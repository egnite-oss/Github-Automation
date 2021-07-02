# Requirements

Open powershell in admin mode and run 
> .\PreRequisites.ps1

If you get an error saying **cannot be loaded because running scripts is disabled on this system** run 
> Set-ExecutionPolicy -ExecutionPolicy Unrestricted

and then run the above command

Once complete run : 
> python ./GithubAutomate.py

Ensure the names of the headings in the Excel sheet match to that of the values in config file as shown : 
![img](./images/config.png)
![img](./images/excel.png)

Get the token from Postman and paste it when prompted( Refer [link](https://onedrive.live.com/view.aspx?resid=C1C67B89C924B584%211772&id=documents&wd=target%28Git%20Automation.one%7CEE518B53-14F3-4574-AB70-C72106A3E645%2FPostman%20configuring%20OAuth%202.0%7C7134C5C5-E54F-4297-BCD8-8BA939782843%2F%29onenote:https://d.docs.live.net/c1c67b89c924b584/Documents/Egnit/Git%20Automation.one#Postman%20configuring%20OAuth%202.0&section-id={EE518B53-14F3-4574-AB70-C72106A3E645}&page-id={7134C5C5-E54F-4297-BCD8-8BA939782843}&end) )
Enter the location of the Excel sheet and the sheet name when prompted.
