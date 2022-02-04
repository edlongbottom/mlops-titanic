import requests
import json

# test POST requst to prediction web service
response = requests.post(url="http://127.0.0.1:5000/titanic/v0.0.1/predict", 
                        headers={"Content-Type": "application/json"}, 
                        data=json.dumps({'PassengerId':[892],'Pclass':[3],'Name':['Kelly, Mr. James'],'Sex':['male'],
                                        'Age':[34.5],'SibSp':[0],'Fare':[7.8292],'Embarked':['S']}))

# run tests
print(response.json()) 
assert len(response.json()) == 1
assert isinstance(response.json()['predictions'],list)
assert response.json()['predictions'][0] in [0,1]