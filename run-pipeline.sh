sudo docker build -t gcr.io/kubernetes-screen-173105/pipeline pipeline
sudo gcloud docker -- push gcr.io/kubernetes-screen-173105/pipeline:latest
gcloud container clusters create kubernetes-screen --scopes bigquery
bq mk database
bq mk -t database.values schema.json
kubectl create -f redis.yaml
kubectl create -f redis-service.yaml
sleep 1
kubectl create -f consumer.yaml
sleep 1 
kubectl create -f producer.yaml