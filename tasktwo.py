from my_utils.csv import HandleCSV
from datetime import datetime

if __name__ =="__main__":
    print("name")

    obj = HandleCSV()
    list1 = HandleCSV.GetData()
    Dict = {}
    for emp in list1:
        if 30< int(emp["DEPARTMENT_ID"]) < 110 and int(emp["SALARY"])>4200:
            name = emp["FIRST_NAME"]+" "+emp["LAST_NAME"]
            HireDate = emp["HIRE_DATE"]
            date = datetime.strptime(HireDate,"%d-%b-%y")
            result = str(date.date())
            Dict[result] = [name]
            Dict.update({result:[name]})
        print(Dict)