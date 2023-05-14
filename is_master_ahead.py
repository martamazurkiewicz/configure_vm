import json
import os
import requests

project = os.environ['SYSTEM_TEAMPROJECT']
organization = os.environ['SYSTEM_TEAMFOUNDATIONCOLLECTIONURI']
repo = os.environ['BUILD_REPOSITORY_NAME']
branch = os.environ['SYSTEM_PULLREQUEST_SOURCEBRANCH']
token = os.environ['SYSTEM_ACCESSTOKEN']
headers = {"Authorization": "Bearer " + token}
commit_url = organization + project  + "/_apis/git/repositories/" + repo + "/commits?searchCriteria.itemVersion.version=master"
commit_response = requests.get(commit_url, headers=headers)
print(commit_response)
# latestcommitid = json.loads(comresponse)['value']['commitid'][0]
# behindurl =OrgUri + project  + "/_apis/git/repositories/" + Repo + "/stats/branches?baseVersionDescriptor.versionOptions=none&baseVersionDescriptor.version=" + latestcommitid + "&baseVersionDescriptor.versionType=commit&api-version=5.1"

# response = requests.get(behindurl, headers=headers)
# print(response)

