#!/usr/bin/env python
"""Consumer that pulls redis queue and writes results to
   big query and then exits when queue is empty.
"""
import os

from apiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import redis

REDIS_HOST = os.environ['REDISMASTER_SERVICE_HOST']
REDIS_PORT = os.environ['REDISMASTER_SERVICE_PORT']
REDIS_LIST = os.environ['REDISLIST']
HOSTNAME = os.environ['HOSTNAME']
PROJECT_ID = os.environ['PROJECT_ID']
BQ_SCOPES = ['https://www.googleapis.com/auth/bigquery']
PRODUCER_DONE = 'PRODUCER_DONE'

NUM_RETRIES = 3

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def create_bigquery_client():
    """Build the bigquery client."""
    credentials = GoogleCredentials.get_application_default()
    if credentials.create_scoped_required():
        credentials = credentials.create_scoped(BQ_SCOPES)
    http = httplib2.Http()
    credentials.authorize(http)
    return discovery.build('bigquery', 'v2', http=http)

def bq_data_insert(bigquery, project_id, dataset, table, value):
    """Insert a list of tweets into the given BigQuery table."""
    try:
        rowlist = []
        # Generate the data that will be sent to BigQuery
        item = {u'value': value, u'pod_name': HOSTNAME}
        item_row = {"json": item}
        rowlist.append(item_row)
        body = {"rows": rowlist}
        # Try the insertion.
        response = bigquery.tabledata().insertAll(
            projectId=project_id, datasetId=dataset,
            tableId=table, body=body).execute(num_retries=NUM_RETRIES)
        return response
    except Exception, e1:
        print "Giving up: %s" % e1

def run_consumer(bigquery):
    redis_errors = 0
    allowed_redis_errors = 3
    while True:
        # Get a value from the buffer
        value = None
        try:
            value = r.brpop(REDIS_LIST)
        except:
            print 'Problem getting data from Redis.'
            redis_errors += 1
            if redis_errors > allowed_redis_errors:
                print "Too many redis errors: exiting."
                return
            continue
        # Write to shared database
        bq_data_insert(bigquery, PROJECT_ID, os.environ['BQ_DATASET'],
                       os.environ['BQ_TABLE'], int(value[1]))
        # Check if can exit
        if r.llen(REDIS_LIST) == 0 and r.exists(PRODUCER_DONE):
            return

if __name__ == '__main__':
    print "Starting consumer.."
    bq = create_bigquery_client()
    run_consumer(bq)