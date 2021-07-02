import pandas, json

class StudentData:
    path= ""
    sheetName = "Sheet1"
    configFile = {}
    studentEmail = {}
    teamName = {}
    gitHandle = {}
    studentId = {}

    def __init__(self):
       self.path = input("Enter the path to student data excel file : ")
       self.sheetName = input("Enter the sheet name")
       f = open('config.json')
       self.configFile = json.load(f)

    def convertSheetToJson(self):
        excel_data_fragment = pandas.read_excel(self.path, sheet_name=self.sheetName)
        studentDataJson = json.loads(excel_data_fragment.to_json())

        self.studentEmail = studentDataJson[self.configFile["StudentEmail"]]
        self.teamName = studentDataJson[self.configFile["TeamName"]]
        self.gitHandle = studentDataJson[self.configFile["GithubHandle"]]
        self.studentId = studentDataJson[self.configFile["StudentId"]]
