
# Design

iOS -> shortcuts app 
Add automation - when homesafeview is opened - action "Get Contents of Url" https://australia-southeast2-puthiye.cloudfunctions.net/<fun_name>
This gcp cloud function will write "open" to bucket swann-config/status

The controller.py reads the "status" file content to decide whether to enable eth1 interface in router (for swann dvr).
After a delay, it invokes the disable eth1 command in router.

# Service account key / json file creation

Go to Google Cloud -> IAM & Admin > Service Accounts

Click on Create Service Accounts

Give the service account name of "sa-bucket" 

Under the section of "Grant this service account access to project"

Then assign role Storage Object Admin
 
If you want to assign more permissions, then go IAM (not Service Accounts) and select sa-bucket.

Goto service account -> Keys -> Add keys - download JSON file

# Platform build
For raspberry pi - create the docker build in pi so that arm64 platform will be used.
Docker builds generated on x86 platforms will not work on ARM based chips.
