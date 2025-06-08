import logging
from locust import HttpUser, task, between
from config.settings import HOST

# Logs configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

class GetPostsUser(HttpUser):
    wait_time = between(1, 2)
    host = HOST

    @task
    def get_posts(self):
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code == 200:
                logger.info(f"Succesful - GET {response.url} - Status Code {response.status_code}")
                response.success()
            else:
                logger.error(
                    f"Error - GET {response.url} - Status Code {response.status_code} - "
                    f"Response: {response.text}"
                )
                response.failure(f"Unexpected Code: {response.status_code}")