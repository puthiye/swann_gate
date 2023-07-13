
# Design

iOS -> shortcuts app 
Add automation - when homesafeview is opened - action "Get Contents of Url" https://australia-southeast2-puthiye.cloudfunctions.net/swann_gate
This GCP cloud function will write "open" to bucket swann_config/status

The controller.py reads the "status" file content to decide whether to enable eth1 link (for swann dvr)
After a delay, it invokes the disable eth1 command.

# Service account key / json file creation

Go to Google Cloud -> IAM & Admin > Service Accounts

Click on Create Service Accounts

Give the service account name of "sa-bucket" 

Under the section of "Grant this service account access to project"

Then assign role Storage Object Admin
 
If you want to assign more permissions, then go IAM (not Service Accounts) and select sa-bucket.

Goto service account -> Keys -> Add keys - download JSON file
