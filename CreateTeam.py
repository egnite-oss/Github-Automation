import requests, json

class Teams:
    URL = "https://api.github.com/orgs/Egnite-git/teams"
    auth_token = ""

    def __init__(self, authToken):
       self.auth_token = authToken

    def createTeam(self, name):
        body = {
            'name':name,
            'description':'This team was created by python script',
            'privacy':'closed',
            'maintainers':["egnite-oss"]
        }

        headers = {
            'accept': 'application/vnd.github.v3+json',
            'authorization': 'Bearer '+self.auth_token
        }

        r = requests.post(self.URL, data=json.dumps(body), headers=headers)

        responseJson = r.json()
        return responseJson['id']

