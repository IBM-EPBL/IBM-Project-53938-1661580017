from locust import HttpUser, task
import random

data = ({'greScore': 400, 'toeflScore': 110, 'univRank': 2, 'sop': 4.5, 'lor': 3.5, 'cgpa': 8.20, 'research': 2}, 
{'greScore': 350, 'toeflScore': 100, 'univRank': 10, 'sop': 2.0, 'lor': 1.0, 'cgpa': 7.00, 'research': 1}, 
{'greScore': 450, 'toeflScore': 102, 'univRank': 1, 'sop': 4.0, 'lor': 4.0, 'cgpa': 9.50, 'research': 4})
post_headers={'Content-Type': 'application/x-www-form-urlencoded'}

class UniversityAdmitEligibilityPredictor(HttpUser):
    @task
    def home_page_test(self):
        self.client.get("/")

    @task
    def checkEligibility_page_test(self):
        self.client.get("/checkEligibility")

    @task
    def predict_page_test(self):
        self.client.post("/predict", data=data[random.randint(0, 2)], headers=post_headers)
