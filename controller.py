import time
import os
import subprocess
from google.cloud import storage

#delay in minutes
off_delay=5 

# service account key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'sa-bucket-key.json'

def download_cs_file(bucket_name, file_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_file_name)


def upload_cs_file(bucket_name, source_file_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)


def is_gate_open():

    #if status file has open, return true
    download_cs_file("swann-config", "status", "tmp")
    with open('tmp') as f:
         file_content = f.read().splitlines()

    if "open" in file_content:
        return True
    else:
        return False


def main():

    print('INFO::: starting swann_gate app...')

    while True:

        if is_gate_open():
            print('INFO::: enabling swann external access..')
            subprocess.call(['sh', './eth1_enable.sh'])
            #once opened, reset the status by writing close to bucket file
            upload_cs_file("swann-config", "status_closed", "status")

        else:
            time.sleep(off_delay)
            print('INFO::: disabling swann external access..')
            subprocess.call(['sh', './eth1_disable.sh'])



if __name__ == "__main__":
    main()
