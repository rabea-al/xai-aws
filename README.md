<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>

<p align="center"><i>Xircuits Component Library for AWS! Seamlessly integrate AWS services into your Xircuits workflows.</i></p>

---

## Xircuits Component Library for AWS

This component library provides AWS service integrations for Xircuits, including support for SQS, S3, and DynamoDB operations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Installation](#installation)

## Prerequisites

Before you begin, make sure you have the following:

1. Python 3.9+.
2. Xircuits.
3. An AWS account with appropriate credentials configured.
4. Python's `boto3` library installed.

## Main Xircuits Components

### SQS Components
- **SQSSendMessage Component**: Sends a message to an SQS queue.

    <img src="https://github.com/user-attachments/assets/a771a580-3338-4f36-a98a-36ae46fe7978" alt="Image" width="200" height="125" />

- **SQSReceiveMessage Component**: Receives messages from an SQS queue.
- **SQSDeleteMessage Component**: Deletes a message from an SQS queue.

### S3 Components
- **S3UploadFile Component**: Uploads a file to an S3 bucket.

    <img src="https://github.com/user-attachments/assets/44f79c47-0588-4811-827d-9338da92aa61" alt="Image" width="200" height="150" />

- **S3DownloadFile Component**: Downloads a file from an S3 bucket.
- **S3ListObjects Component**: Lists objects in an S3 bucket.

### DynamoDB Components
- **DynamoDBPutItem Component**: Inserts an item into a DynamoDB table.
- **DynamoDBGetItem Component**: Retrieves an item from a DynamoDB table.
- **DynamoDBDeleteItem Component**: Deletes an item from a DynamoDB table.

### AWS Glue Components
- **GlueStartJobRun Component**: Starts an AWS Glue job run.
- **GetGlueJobStatus Component**: Retrieves the status of an AWS Glue job run.

### AWS Bedrock Components
- **AWSBedrockClient Component**: Initializes a Bedrock client.
- **AWSBedrockListModels Component**: Lists available models from Bedrock.
- **AWSBedrockInvokeAnthropicModel Component**: Invokes a model hosted on AWS Bedrock.
  

## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the AWS library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install aws
```

You can also install it manually by cloning the repository:

```
# base Xircuits directory

git clone https://github.com/XpressAI/xai-aws xai_components/xai_aws
pip install -r xai_components/xai_aws/requirements.txt
```

