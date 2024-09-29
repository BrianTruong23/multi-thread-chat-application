import logging
from locust import HttpUser, TaskSet, task, between

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserBehavior(TaskSet):
    @task
    def send_message(self):
        try:
            response = self.client.post("/send", json={"message": "Hello, server!"})
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response text: {response.text}")
        except Exception as e:
            logger.error(f"Request failed: {e}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=http://127.0.0.1:12345")
