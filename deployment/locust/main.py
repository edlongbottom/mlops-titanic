from locust import HttpUser, task, constant

class LoadTest(HttpUser):
    wait_time = constant(0)
    host = "http://10.100.244.233"

    @task
    def predict(self):
        request_body = {
            'PassengerId':[892],
            'Pclass':[3],
            'Name':['Kelly, Mr. James'],
            'Sex':['male'],
            'Age':[34.5],
            'SibSp':[0],
            'Fare':[7.8292],
            'Embarked':['S']
        }

        self.client.post(
            "http://10.100.244.233:5000/titanic/v0.0.1/predict", json=request_body
        )
