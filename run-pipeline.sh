# Build the docker image and deploy it to the google container registry
sudo docker build -t gcr.io/kubernetes-screen-173105/pipeline pipeline
sudo gcloud docker -- push gcr.io/kubernetes-screen-173105/pipeline:latest

# Start up GKE cluster with bigquery in its NODESCOPE so it can write to the 
# database
gcloud container clusters create kubernetes-screen --scopes bigquery

# Create a BigQuery database and instaniate a table with the schema in
# schema.json
bq mk database
bq mk -t database.values schema.json

# Start the pipeline 
kubectl create -f redis.yaml
kubectl create -f redis-service.yaml
kubectl create -f consumer.yaml
kubectl create -f producer.yaml
