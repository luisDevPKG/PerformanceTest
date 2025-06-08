import logging
from locust import HttpUser, task, between
from config.settings import HOST
import json

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
        endpoint = "/posts"
        logger.info("Executing")
        with self.client.get(endpoint, catch_response=True) as response:
            if response.status_code == 200:
                try:
                    data = response.json()
                    if isinstance(data, list) and len(data) == 100:
                        logger.info(
                            f"Successful: GET {response.url} - Status Code: {response.status_code} - "
                            f"Posts received: {len(data)}"
                        )
                        logger.info("Response Json:\n" + json.dumps(data[3], indent=2))
                        response.success()
                    elif isinstance(data, list):
                        logger.warning(
                            f"Incorrect Quantity: GET {response.url} - Status Code: {response.status_code}"
                        )
                        response.failure(f"100 posts were expected. They just arrived: {len(data)}")
                    else:
                        logger.error(
                            f"Format Error: GET {response.url} - Status Code: {response.status_code}"
                            f"Content (200 chars): {response.text[:200]}"
                        )
                        response.failure(f"Answer is not a list. The type is: {type(data)}")
                except ValueError:
                    logger.error(
                        f"Json Error: GET {response.url} - Status Code: {response.status_code}"
                        f"Failed to decode response as JSON"
                        f"Content (200 chars): {response.text[:200]}"
                    )
                    response.failure("Response is not valid JSON")
            else:
                logger.error(
                    f"Http Error: GET {response.url} - Status Code: {response.status_code}"
                    f"Content (200 chars): {response.text[:200]}"
                )
                response.failure(f"Unexpected HTTP code: {response.status_code}")
