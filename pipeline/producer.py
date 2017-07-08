#!/usr/bin/env python
"""Producer that writes values 1 to 1000 to redis queue and then signals
   completion.
"""
import os
import redis

REDIS_HOST = os.environ['REDISMASTER_SERVICE_HOST']
REDIS_PORT = os.environ['REDISMASTER_SERVICE_PORT']
REDIS_LIST = 'BUFFER'
PRODUCER_DONE = 'PRODUCER_DONE'


if __name__ == '__main__':
    
    redis_errors = 0
    allowed_redis_errors = 3
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    for i in range(1, 1000):
        try:
            r.lpush(REDIS_LIST, '%s' % i)
        except:
            print 'Problem adding data to Redis.'
            redis_errors += 1

        if redis_errors > allowed_redis_errors:
            print 'too many redis errors.'
            break

    r.lpush(PRODUCER_DONE, "DONE")