A simple producer consumer pipeline.

Before running, you'll need to replace all instances of the project-id, "kubernetes-screen-173105" with your own Google Cloud Engine project-id. 

To run:
    
    $./run-pipeline.sh

To clean-up:

    $./clean-up-pipeline.sh

For an example of the database contents after running the pipeline see
results.csv.

To query the database:

    $bq query \
        'SELECT * FROM [kubernetes-screen-173105:database.values] LIMIT 1000'