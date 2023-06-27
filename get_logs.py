import requests
import json

# Azure DevOps organization URL
org_url = "https://dev.azure.com/{organization}"

# Personal access token (PAT)
pat = "{personal_access_token}"

# Build ID
build_id = "{build_id}"

# Get timeline API URL
timeline_url = f"{org_url}/DefaultCollection/_apis/build/builds/{build_id}/timeline?api-version=6.0"

# Send GET request to get the timeline
response = requests.get(timeline_url, auth=("", pat))

# Parse the response JSON
timeline = json.loads(response.text)

# Extract the job records from the timeline
job_records = [r for r in timeline["records"] if r["type"] == "Job"]

# Extract the log IDs from the job records
log_ids = [r["log"]["id"] for r in job_records]

# Print the log IDs
print(log_ids)