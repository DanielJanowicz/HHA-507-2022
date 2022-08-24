# Data Ingestion

## First steps 
- Create virtual environment `python3 -m venv {nameofvirtualenv}`
- Activate the virtual environment `source {nameofvirtualenv}/bin/activate` 
- Install packages found in requirements.txt into virtual environment `pip3 install -r requirements.txt` 
- Go through each line in python file `ingestion\ingestion.py` and check it out! 

## Bigquery setup 
- tutorial here -> need to create service file (.json) that contains credentials: https://cloud.google.com/bigquery/docs/reference/libraries#setting_up_authentication 
- role type, `editor` - should give enough permissions 
- create new key (.json) type and save it into ingestion/example_files/bigquery 