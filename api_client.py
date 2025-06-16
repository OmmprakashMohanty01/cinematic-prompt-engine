import json
import logging
import requests

logger = logging.getLogger(__name__)


import requests


class LLMService:
    def __init__(self, api_url, api_key):
        """
        Initialize the LLMService class with API information.

        Args:
            api_url (str): The URL of the API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def send_prompt(self, prompt):
        """
        Send a formatted text prompt to the external LLM or image generation API.

        Args:
            prompt (str): The formatted text prompt to be sent.

        Returns:
            str: The response from the API.
        """
        params = {"prompt": prompt, "api_key": self.api_key}

        response = requests.post(self.api_url, params=params)

        if response.status_code == 200:
            return response.text
        else:
            raise Exception(
                f"Failed to send prompt. Status code: {response.status_code}"
            )


class LLMModel:
    def __init__(self, model_name):
        """
        Initialize the LLMModel class with model information.

        Args:
            model_name (str): The name of the LLM model.
        """
        self.model_name = model_name

    def get_model_description(self):
        """
        Get a description of the LLM model.

        Returns:
            str: The description of the LLM model.
        """
        params = {"model_name": self.model_name, "api_key": self.api_key}

        response = requests.get(f"{self.api_url}/models", params=params)

        if response.status_code == 200:
            return response.json()["description"]
        else:
            raise Exception(
                f"Failed to get model description. Status code: {response.status_code}"
            )
