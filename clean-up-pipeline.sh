kubectl delete -f producer.yaml
kubectl delete -f consumer.yaml
kubectl delete -f redis-service.yaml
kubectl delete -f redis.yaml
bq rm -f -t database.values
bq rm -f database
gcloud container clusters delete kubernetes-screen