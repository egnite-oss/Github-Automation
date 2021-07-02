import requests, json

class CreateRepositories:
    URL = "https://api.github.com/orgs/Egnite-git/repos"
    auth_token = ""
    def __init__(self, authToken):
       self.auth_token = authToken

    def getRepositoryName(self, studentGitHandle, studentId, teamName):
        myTuple = (studentGitHandle, str(studentId), teamName)
        return "-".join(myTuple)

    def createRepository(self, repoName, teamId):
        body = {
            "name": repoName,
            "description": "This repo is created by automation",
            "team_id": teamId,
            "auto_init": True,
            "license_template": "mit"
        }

        headers = {
            'accept': 'application/vnd.github.v3+json',
            'authorization': 'Bearer '+self.auth_token
        }

        r = requests.post(self.URL, data=json.dumps(body), headers=headers)

        responseJson = r.json()
        return responseJson['id']

