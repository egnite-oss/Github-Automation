from StudentData import StudentData
from CreateTeam import Teams
from SendInvitations import SendInvitations
from CreateRepositories import  CreateRepositories

class GithubAutomate:
    data = []
    loc = "enter the file path"
    
    def __init__(self):
       authToken = input("Enter the auth token : ")
       t = Teams(authToken)
       studentInvitation = SendInvitations(authToken)
       teamData= {}
       repos = CreateRepositories(authToken)
       studentData = StudentData()
       studentData.convertSheetToJson()

       for key, teamName in studentData.teamName.items():
           self.data.append(teamName)
           print(teamName)

       teamNames = set(self.data)

       for teamName in teamNames:
           teamId = t.createTeam(teamName)
           teamData[teamName] = teamId
       
       for key, teamName in studentData.teamName.items():
           studentEmail = studentData.studentEmail[key]
           githubHandle = studentData.gitHandle[key]
           studentId = studentData.studentId[key]

           studentInvitation.sendInvite(studentEmail, teamData[teamName])
           repoName = repos.getRepositoryName(githubHandle, studentId, teamName)
           repos.createRepository(repoName, teamData[teamName])

p1 = GithubAutomate()