import requests, json

class SendInvitations:
    URL = "https://api.github.com/orgs/Egnite-git/invitations"
    auth_token = ""

    def __init__(self, authToken):
       self.auth_token = authToken

    def sendInvite(self, email, teamId):
        body = {
            'email':email,
            'team_ids': [teamId]
        }

        headers = {
            'accept': 'application/vnd.github.v3+json',
            'authorization': 'Bearer '+self.auth_token
        }

        r = requests.post(self.URL, data=json.dumps(body), headers=headers)

        responseJson = r.json()
        return responseJson['id']

