import requests

from utils.logger import get_logger


logger = get_logger()


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, headers=None, params=None):

        logger.info(f"Sending GET request to: {url}")

        response = self.session.get(
            url,
            headers=headers,
            params=params
        )

        logger.info(
            f"Response Status Code: {response.status_code}"
        )

        return response

    def post(self, url, payload=None, headers=None):

        logger.info(f"Sending POST request to: {url}")

        logger.info(f"Payload: {payload}")

        response = self.session.post(
            url,
            json=payload,
            headers=headers
        )

        logger.info(
            f"Response Status Code: {response.status_code}"
        )

        return response

    def put(self, url, payload=None, headers=None):

        logger.info(f"Sending PUT request to: {url}")

        logger.info(f"Payload: {payload}")

        response = self.session.put(
            url,
            json=payload,
            headers=headers
        )

        logger.info(
            f"Response Status Code: {response.status_code}"
        )

        return response

    def delete(self, url, headers=None):

        logger.info(f"Sending DELETE request to: {url}")

        response = self.session.delete(
            url,
            headers=headers
        )

        logger.info(
            f"Response Status Code: {response.status_code}"
        )

        return response 