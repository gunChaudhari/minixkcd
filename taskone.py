import requests
from my_utils.csv import HandleCSV

filename = "employee.csv"


if __name__ =="__main__":
    """creating object of a class HandleCSV"""
    obj = HandleCSV()
    obj1 = HandleCSV.GetData()

    salary = {}
    for emp in obj1:
        for i,j in emp.items():
            if int(emp["SALARY"])>9000:
                name = emp["FIRST_NAME"]+" "+emp["LAST_NAME"]
                #print(f"name:{name}")
                email = emp["EMAIL"]
                #print(f"email:{email}")
                phone_number = emp["PHONE_NUMBER"]
                #print(f"phone_number:{phone_number}")
                salary.update({"name":name})
                salary.update({"email":email})
                salary.update({"phone_number":phone_number})
            print(salary)