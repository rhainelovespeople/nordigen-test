import requests
import json

accountId = "5a59028c-e757-4f22-b88c-3ba90573383c"
transactionsUrl = "https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/"+accountId+"/transactions?bookingStatus=both"

with open("credentials.json") as credentialsFile:
    credentialsJson = json.load(credentialsFile)
    credentialsFile.close()

headers = {
    'Accept': "application/json",
    'X-Request-ID': "WvqiIbLrevVN82r35UqgS9S1srsENuqI",
    'Authorization': "Bearer " + credentialsJson['bearer_token'],
    'PSU-Http-Method': "GET"
    }

r = requests.get(transactionsUrl, headers=headers)
print(r.text)