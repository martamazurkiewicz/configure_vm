import json
import os
import requests

print('ENV vars')
print(os.environ)
print('----')
project = os.environ['SYSTEM_TEAMPROJECT']
print(project)
organization = os.environ['SYSTEM_TEAMFOUNDATIONCOLLECTIONURI']
print(organization)
repo = os.environ['BUILD_REPOSITORY_NAME']
print(repo)
#branch = os.environ['SYSTEM_PULLREQUEST_SOURCEBRANCH']
branch = os.environ['BUILD_SOURCEBRANCH']
print(branch)
token = os.environ['SYSTEM_ENABLEACCESSTOKEN']
headers = {"Authorization": "Bearer " + token}
print(headers)
commit_url = organization + project  + "/_apis/git/repositories/" + repo + "/commits?searchCriteria.itemVersion.version=master"
print(commit_url)
commit_response = requests.get(commit_url, headers=headers)
print(commit_response)
# latestcommitid = json.loads(comresponse)['value']['commitid'][0]
# behindurl =OrgUri + project  + "/_apis/git/repositories/" + Repo + "/stats/branches?baseVersionDescriptor.versionOptions=none&baseVersionDescriptor.version=" + latestcommitid + "&baseVersionDescriptor.versionType=commit&api-version=5.1"

# response = requests.get(behindurl, headers=headers)
# print(response)

