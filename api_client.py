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


class LLMServiceResponse:
    def __init__(self, response_text):
        self.response_text = response_text

    def as_json(self):
        try:
            return json.loads(self.response_text)
        except json.JSONDecodeError:
            return {}

    def get_output_text(self):
        if self.as_json().get("output"):
            return self.as_json()["output"]
        return ""


def get_model_output(self, prompt):
    response = self.send_prompt(prompt)
    output_response = LLMServiceResponse(response)
    return output_response.get_output_text()


class LLMModelCatalog:
    def __init__(self, api_url, api_key):
        """
        Initialize the LLMModelCatalog class with API information.

        Args:
            api_url (str): The URL of the API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_model_list(self):
        """
        Get a list of available LLM models.

        Returns:
            list: The list of available LLM models.
        """
        params = {"api_key": self.api_key}

        response = requests.get(f"{self.api_url}/models", params=params)

        if response.status_code == 200:
            return response.json()["models"]
        else:
            raise Exception(
                f"Failed to get model list. Status code: {response.status_code}"
            )


class LLMModelInfo:
    def __init__(self, model_info_json):
        self.model_info_json = model_info_json

    def get_model_name(self):
        return self.model_info_json["model_name"]

    def get_model_description(self):
        return self.model_info_json["description"]


def get_model_info(model_name, api_client):
    response = api_client.get_model_list()
    for model in response:
        if model["model_name"] == model_name:
            return model
    raise Exception(f"Model '{model_name}' not found")


class TextGenerationResult:
    def __init__(self, model_name, generated_text):
        """
        Initialize the TextGenerationResult class.

        Args:
            model_name (str): The name of the LLM model that generated the text.
            generated_text (str): The generated text.
        """
        self.model_name = model_name
        self.generated_text = generated_text

    def as_dict(self):
        return {
            "model": self.model_name,
            "generated_text": self.generated_text,
        }


class LLMServiceResult:
    def __init__(self, api_client, prompt, response):
        """
        Initialize the LLMServiceResult class.

        Args:
            api_client (LLMService): The api client instance.
            prompt (str): The original prompt sent to the LLM API.
            response (str): The response from the LLM API.
        """
        self.api_client = api_client
        self.prompt = prompt
        self.response = response

    def get_result(self):
        try:
            result = LLMServiceResponse(self.response).as_json()
            return TextGenerationResult(
                self.api_client.model_name, result.get("output", "")
            )
        except Exception as e:
            return f"Failed to generate text: {str(e)}"

    def as_dict(self):
        return {
            "prompt": self.prompt,
            "result": self.get_result().as_dict(),
        }


def get_results(api_client, prompts):
    results = []
    for prompt in prompts:
        response = api_client.send_prompt(prompt)
        results.append(LLMServiceResult(api_client, prompt, response))
    return results


class ImageGenerationResult:
    def __init__(self, model_name, generated_image_url):
        """
        Initialize the ImageGenerationResult class.

        Args:
            model_name (str): The name of the LLM model that generated the image.
            generated_image_url (str): The URL of the generated image.
        """
        self.model_name = model_name
        self.generated_image_url = generated_image_url

    def as_dict(self):
        return {
            "model": self.model_name,
            "generated_image_url": self.generated_image_url,
        }


class ImageGenerationResultAPI:
    def __init__(self, api_client, image_url):
        """
        Initialize the ImageGenerationResult class.

        Args:
            api_client (LLMService): The api client instance.
            image_url (str): The URL of the generated image.
        """
        self.api_client = api_client
        self.image_url = image_url

    def get_result(self):
        try:
            result = ImageGenerationResult(self.api_client.model_name, self.image_url)
            return result
        except Exception as e:
            return f"Failed to generate image: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        result["prompt"] = self.api_client.prompt
        return result


def get_image_results(api_client, image_prompts):
    results = []
    for image_prompt in image_prompts:
        response = api_client.send_prompt(image_prompt)
        image_url = response.get("generated_image", "")
        results.append(ImageGenerationResultAPI(api_client, image_url))
    return results


class LLMServiceError(Exception):
    """
    Custom exception class for LLMService related errors.
    """

    pass


class ModelNotFoundError(LLMServiceError):
    """
    Custom exception class for when a model is not found.
    """

    pass


class APIConnectionError(LLMServiceError):
    """
    Custom exception class for when there is a problem with the API connection.
    """

    pass


class TextCompletionResult:
    def __init__(self, model_name, completion_text):
        """
        Initialize the TextCompletionResult class.

        Args:
            model_name (str): The name of the LLM model that generated the text.
            completion_text (str): The completed text.
        """
        self.model_name = model_name
        self.completion_text = completion_text

    def as_dict(self):
        return {
            "model": self.model_name,
            "completion_text": self.completion_text,
        }


class TextCompletionResultAPI:
    def __init__(self, api_client, completion_text):
        """
        Initialize the TextCompletionResult class.

        Args:
            api_client (LLMService): The api client instance.
            completion_text (str): The completed text.
        """
        self.api_client = api_client
        self.completion_text = completion_text

    def get_result(self):
        try:
            result = TextCompletionResult(
                self.api_client.model_name, self.completion_text
            )
            return result
        except Exception as e:
            return f"Failed to generate text: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        result["prompt"] = self.api_client.prompt
        return result


def get_completion_results(api_client, completion_prompts):
    results = []
    for prompt in completion_prompts:
        response = api_client.send_prompt(prompt)
        completion_response = {
            "completion_response": LLMServiceResponse(response)
            .as_json()
            .get("completion_text", "")
        }
        results.append(
            TextCompletionResultAPI(
                api_client, completion_response["completion_response"]
            )
        )
    return results


class TranslationResult:
    def __init__(self, model_name, translated_text):
        self.model_name = model_name
        self.translated_text = translated_text

    def as_dict(self):
        return {
            "model": self.model_name,
            "translated_text": self.translated_text,
        }


class TranslationResultAPI:
    def __init__(self, api_client, translated_text):
        self.api_client = api_client
        self.translated_text = translated_text

    def get_result(self):
        try:
            result = TranslationResult(self.api_client.model_name, self.translated_text)
            return result
        except Exception as e:
            return f"Failed to translate text: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        result["prompt"] = self.api_client.prompt
        return result


def get_translation_results(api_client, translation_prompts):
    results = []
    for prompt in translation_prompts:
        response = api_client.send_prompt(prompt)
        params = {"input_text": response, "model_name": api_client.model_name}
        response = requests.post(f"{api_client.api_url}/translate", params=params)
        if response.status_code == 200:
            result = TranslationResultAPI(api_client, response.text)
            results.append(result.as_dict())
        else:
            raise Exception(
                f"Failed to translate text. Status code: {response.status_code}"
            )
    return results


class ConversationResult:
    def __init__(self, model_name, conversation_history):
        self.model_name = model_name
        self.conversation_history = conversation_history

    def as_dict(self):
        return {
            "model": self.model_name,
            "conversation_history": self.conversation_history,
        }


class ConversationResultAPI:
    def __init__(self, api_client, conversation_history):
        self.api_client = api_client
        self.conversation_history = conversation_history

    def get_result(self):
        try:
            result = ConversationResult(
                self.api_client.model_name, self.conversation_history
            )
            return result
        except Exception as e:
            return f"Failed to generate conversation history: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        result["prompt"] = self.api_client.prompt
        return result


def get_conversation_results(api_client, conversation_prompts):
    results = []
    for prompt in conversation_prompts:
        response = api_client.send_prompt(prompt)
        response_json = LLMServiceResponse(response).as_json()
        if response_json.get("nextPrompt"):
            next_prompt = response_json["nextPrompt"]
            conversation_history = response_json.get("conversation_history", [])
            response = requests.post(
                f"{api_client.api_url}/conversation", json={"prompt": next_prompt}
            )
            if response.status_code == 200:
                result_json = response.json()
                conversation_history.append(
                    f"{response_json['userInput']} - {response_json['assistantResponse']}"
                )
                conversation_history.append(
                    f"{next_prompt} - {result_json.get('assistantResponse', '')}"
                )
                result = ConversationResultAPI(api_client, conversation_history)
                results.append(result.as_dict())
            else:
                raise Exception(
                    f"Failed to continue conversation. Status code: {response.status_code}"
                )
        else:
            raise Exception(f"Conversation has ended.")
    return results


class ModelListResult:
    def __init__(self, models):
        self.models = models

    def as_dict(self):
        return {
            "models": self.models,
        }


class ModelListResultAPI:
    def __init__(self, models):
        self.models = models

    def get_result(self):
        try:
            result = ModelListResult(self.models)
            return result
        except Exception as e:
            return f"Failed to retrieve model list: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        return result


def get_model_list(api_client):
    response = requests.get(f"{api_client.api_url}/models")
    if response.status_code == 200:
        try:
            result = response.json()
            return ModelListResultAPI(result["models"])
        except json.JSONDecodeError:
            raise Exception(
                f"Failed to decode model list. Status code: {response.status_code}"
            )
    else:
        raise Exception(
            f"Failed to retrieve model list. Status code: {response.status_code}"
        )


class ModelStatusResult:
    def __init__(self, model_name, status):
        self.model_name = model_name
        self.status = status

    def as_dict(self):
        return {
            "model": self.model_name,
            "status": self.status,
        }


class ModelStatusResultAPI:
    def __init__(self, model_name, status_url):
        self.model_name = model_name
        self.status_url = status_url

    def get_result(self):
        try:
            result = ModelStatusResult(self.model_name, None)
            return result
        except Exception as e:
            return f"Failed to retrieve model status: {str(e)}"

    def as_dict(self):
        result = self.get_result().as_dict()
        result["status_url"] = self.status_url
        return result


def get_model_status(api_client, model_name):
    response = requests.get(f"{api_client.api_url}/models/{model_name}/status")
    if response.status_code == 200:
        result = ModelStatusResultAPI(model_name, response.url)
        return result.as_dict()
    else:
        raise Exception(
            f"Failed to retrieve model status. Status code: {response.status_code}"
        )
