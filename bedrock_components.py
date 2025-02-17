from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component
import boto3
import json
from typing import Any, Union

@xai_component(color="blue")
class AWSBedrockClient(Component):
    """Component to initialize a Bedrock client.

    ##### inPorts:
    - region_name (str): The AWS region where the Bedrock service is hosted.

    ##### outPorts:
    - bedrock_client (Any): The initialized Bedrock client instance.
    """
    region_name: InCompArg[str]
    bedrock_client: OutArg[Any]

    def execute(self, ctx) -> None:
        self.bedrock_client.value = boto3.client(service_name="bedrock-runtime", region_name=self.region_name.value)
        ctx["bedrock_client"] = self.bedrock_client.value
        print(f"Initialized Bedrock client in region: {self.region_name.value}")

@xai_component(color="blue")
class AWSBedrockListModels(Component):
    """Component to list available models from Bedrock.

    ##### inPorts:
    - bedrock_client (Any): The initialized Bedrock client instance.

    ##### outPorts:
    - model_list (list): A list of available model IDs.
    """
    bedrock_client: InArg[Any]
    model_list: OutArg[list]

    def execute(self, ctx) -> None:
        client = self.bedrock_client.value if self.bedrock_client.value else ctx.get("bedrock_client")
        if not client:
            raise ValueError("Bedrock client not provided and not found in context.")
        
        response = client.list_foundation_models(byProvider="anthropic")
        self.model_list.value = [summary["modelId"] for summary in response["modelSummaries"]]
        print("Available models:")
        for model_id in self.model_list.value:
            print(model_id)

@xai_component(color="blue")
class AWSBedrockInvokeAnthropicModel(Component):
    """Component to invoke a model hosted on AWS Bedrock.

    ##### inPorts:
    - bedrock_client (Any): The initialized Bedrock client instance.
    - model_id (str): The ID of the model to invoke.
    - user_message (str): The user message to send to the model.
    - max_tokens (int): The maximum number of tokens in the model response. Defaults to 512.

    ##### outPorts:
    - response_content (str): The content of the model's response.
    """
    bedrock_client: InArg[Any]
    model_id: InCompArg[str]
    user_message: InCompArg[str]
    max_tokens: InCompArg[int]
    response_content: OutArg[str]

    def __init__(self):
        super().__init__()
        self.max_tokens.value = 512

    def execute(self, ctx) -> None:
        client = self.bedrock_client.value if self.bedrock_client.value else ctx.get("bedrock_client")
        if not client:
            raise ValueError("Bedrock client not provided and not found in context.")

        body = json.dumps({
            "max_tokens": self.max_tokens.value,
            "messages": [{"role": "user", "content": self.user_message.value}],
            "anthropic_version": "bedrock-2023-05-31"
        })

        response = client.invoke_model(body=body, modelId=self.model_id.value)
        response_body = json.loads(response.get("body").read())
        self.response_content.value = response_body.get("content")

        print(f"Model Response: {self.response_content.value}")
