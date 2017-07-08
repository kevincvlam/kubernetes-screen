A simple producer consumer pipeline.

To run make sure you have a cluster available to use:

    $ gcloud container clusters create kubernetes-screen --scopes bigquery

Then setup a bigquery dataset and table:

    $ ./setup_bq.sh

Setup the buffer and consumers:
    
    $ ./setup_inputs_and_consumers.sh

Run the producer:

    $ ./run_producer.sh

Dump Shared Database Table:
    
    $

Clean-up:

    $ gcloud container clusters delete kubernetes-screen

Updating docker image

    $ sudo docker build -t gcr.io/kubernetes-screen-173105/pipeline:vX pipeline
    $ sudo gcloud docker -- push gcr.io/kubernetes-screen-173105/pipeline:vX