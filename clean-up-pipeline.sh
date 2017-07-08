# Clean-up completed pods
kubectl delete -f producer.yaml
kubectl delete -f consumer.yaml
kubectl delete -f redis-service.yaml
kubectl delete -f redis.yaml

# Clean-up shared database
bq rm -f -t database.values
bq rm -f database

# Turn down cluster
gcloud container clusters delete kubernetes-screen