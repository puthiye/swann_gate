from google.cloud import storage
import functions_framework
import json

def swann_config(request):
    # The ID of your GCS bucket
    bucket_name = "swann-config"

    # The ID of your new GCS object
    blob_name = "status"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with blob.open("w") as f:
        f.write("open")

    return { 
            'statusCode': 200,
            'body': json.dumps('Success')
        }
