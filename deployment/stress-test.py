import requests, json, time

# define base URL (localhost + flask port)
url = "http://127.0.0.1:65169/titanic/v0.0.1/predict"
headers = {"Content-Type": "application/json"}
body = {'PassengerId':[892],'Pclass':[3],'Name':['Kelly, Mr. James'],'Sex':['male'],
        'Age':[34.5],'SibSp':[0],'Fare':[7.8292],'Embarked':['S']}

# send a POST request to flask api
x=0
while x < 10000000:
    response = requests.post(url=url, data=json.dumps(body), headers=headers)
    print(response.json()) 
    time.sleep(0.001)
    x+=1