# Xircuits AWS Components

This component library provides AWS service integrations for Xircuits, including support for SQS, S3, and DynamoDB operations.

## Prerequisites

- An AWS account with appropriate credentials configured
- Python's `boto3` library
- Xircuits installed in your environment

## Installation

To use this component library, ensure you have Xircuits installed, then simply run:

```
xircuits install git@github.com:XpressAI/xai-aws.git
```

Alternatively you may manually copy the directory / clone or submodule the repository to your working Xircuits project directory then install the packages using:

```
pip install -r requirements.txt
```

## Components

### SQS Components
- `SendMessage`: Send a message to an SQS queue
- `ReceiveMessage`: Receive messages from an SQS queue
- `DeleteMessage`: Delete a message from an SQS queue

### S3 Components
- `UploadFile`: Upload a file to an S3 bucket
- `DownloadFile`: Download a file from an S3 bucket
- `ListObjects`: List objects in an S3 bucket

### DynamoDB Components
- `DynamoDBPutItem`: Insert an item into a DynamoDB table
- `DynamoDBGetItem`: Retrieve an item from a DynamoDB table
- `DynamoDBDeleteItem`: Delete an item from a DynamoDB table

## Tests
A github action to test your workflow runs has been provided. Simply add the path of your workflows [here](.github/workflows/run-workflow-tests.yml#L11).
