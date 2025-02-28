from xai_components.base import InArg, OutArg, Component, xai_component
import boto3


@xai_component
class SQSSendMessage(Component):
    """Component to send a message to an SQS queue.

    ##### inPorts:
    - queue_url (str): The URL of the SQS queue.
    - message_body (str): The message body to send.
    
    ##### outPorts:
    - message_id (str): The ID of the sent message.
    """
    queue_url: InArg[str]
    message_body: InArg[str]
    message_id: OutArg[str]

    def execute(self, ctx) -> None:
        sqs = boto3.client('sqs')
        response = sqs.send_message(
            QueueUrl=self.queue_url.value,
            MessageBody=self.message_body.value
        )
        self.message_id.value = response['MessageId']


@xai_component
class SQSReceiveMessage(Component):
    """Component to receive messages from an SQS queue.

    ##### inPorts:
    - queue_url (str): The URL of the SQS queue.
    - max_message_count (int): The max number of messages to get from the queue.
    - wait_time_secs (int): The amount of time to wait for new messages.
    
    ##### outPorts:
    - messages (list): A list of received messages.
    """
    queue_url: InArg[str]
    max_message_count: InArg[int]
    wait_time_secs: InArg[int]
    messages: OutArg[list]

    def execute(self, ctx) -> None:
        sqs = boto3.client('sqs')
        response = sqs.receive_message(
            QueueUrl=self.queue_url.value,
            MaxNumberOfMessages=self.max_message_count.value if self.max_message_count.value is not None else 10,
            WaitTimeSeconds=self.wait_time_secs if self.wait_time_secs.value is not None else 10
        )
        self.messages.value = response.get('Messages', [])



@xai_component
class SQSDeleteMessage(Component):
    """Component to delete a message from an SQS queue.

    ##### inPorts:
    - queue_url (str): The URL of the SQS queue.
    - receipt_handle (str): The receipt handle of the message to delete.
    """
    queue_url: InArg[str]
    receipt_handle: InArg[str]

    def execute(self, ctx) -> None:
        sqs = boto3.client('sqs')
        sqs.delete_message(
            QueueUrl=self.queue_url.value,
            ReceiptHandle=self.receipt_handle.value
        )


@xai_component
class S3UploadFile(Component):
    """Component to upload a file to an S3 bucket.

    ##### inPorts:
    - bucket_name (str): The name of the S3 bucket.
    - file_path (str): The local path of the file to upload.
    - object_name (str): The name to assign to the file in S3.
    
    ##### outPorts:
    - response (dict): The response from the S3 upload operation.
    """
    bucket_name: InArg[str]
    file_path: InArg[str]
    object_name: InArg[str]
    response: OutArg[dict]

    def execute(self, ctx) -> None:
        s3 = boto3.client('s3')
        response = s3.upload_file(
            Filename=self.file_path.value,
            Bucket=self.bucket_name.value,
            Key=self.object_name.value
        )
        self.response.value = response


@xai_component
class S3DownloadFile(Component):
    """Component to download a file from an S3 bucket.

    ##### inPorts:
    - bucket_name (str): The name of the S3 bucket.
    - object_name (str): The name of the file in S3.
    - file_path (str): The local path to save the downloaded file.
    
    ##### outPorts:
    - response (dict): The response from the S3 download operation.
    """
    bucket_name: InArg[str]
    object_name: InArg[str]
    file_path: InArg[str]
    response: OutArg[dict]

    def execute(self, ctx) -> None:
        s3 = boto3.client('s3')
        response = s3.download_file(
            Bucket=self.bucket_name.value,
            Key=self.object_name.value,
            Filename=self.file_path.value
        )
        self.response.value = response


@xai_component
class S3ListObjects(Component):
    """Component to list objects in an S3 bucket.

    ##### inPorts:
    - bucket_name (str): The name of the S3 bucket.
    
    ##### outPorts:
    - objects (list): A list of objects in the specified S3 bucket.
    """
    bucket_name: InArg[str]
    objects: OutArg[list]

    def execute(self, ctx) -> None:
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket_name.value)
        self.objects.value = response.get('Contents', [])


@xai_component
class DynamoDBPutItem(Component):
    """Component to insert an item into a DynamoDB table.

    ##### inPorts:
    - table_name (str): The name of the table.
    - item (dict): The item to insert (e.g., {'id': {'S': '123'}, 'name': {'S': 'John'}}).
    
    ##### outPorts:
    - response (dict): The response from the PutItem operation.
    """
    table_name: InArg[str]
    item: InArg[dict]
    response: OutArg[dict]

    def execute(self, ctx) -> None:
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.put_item(
            TableName=self.table_name.value,
            Item=self.item.value
        )
        self.response.value = response


@xai_component
class DynamoDBGetItem(Component):
    """Component to retrieve an item from a DynamoDB table.

    ##### inPorts:
    - table_name (str): The name of the table.
    - key (dict): The key of the item to retrieve (e.g., {'id': {'S': '123'}}).
    
    ##### outPorts:
    - item (dict): The retrieved item.
    """
    table_name: InArg[str]
    key: InArg[dict]
    item: OutArg[dict]

    def execute(self, ctx) -> None:
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.get_item(
            TableName=self.table_name.value,
            Key=self.key.value
        )
        self.item.value = response.get('Item', {})


@xai_component
class DynamoDBDeleteItem(Component):
    """Component to delete an item from a DynamoDB table.

    ##### inPorts:
    - table_name (str): The name of the table.
    - key (dict): The key of the item to delete (e.g., {'id': {'S': '123'}}).
    
    ##### outPorts:
    - response (dict): The response from the DeleteItem operation.
    """
    table_name: InArg[str]
    key: InArg[dict]
    response: OutArg[dict]

    def execute(self, ctx) -> None:
        dynamodb = boto3.client('dynamodb')
        response = dynamodb.delete_item(
            TableName=self.table_name.value,
            Key=self.key.value
        )
        self.response.value = response


@xai_component
class GlueStartJobRun(Component):
    """Component to start an AWS Glue job run.

    ##### inPorts:
    - job_name (str): The name of the AWS Glue job.
    - arguments (dict): Optional arguments to pass to the job.

    ##### outPorts:
    - job_run_id (str): The ID of the started job run.
    """
    job_name: InArg[str]
    arguments: InArg[dict]
    job_run_id: OutArg[str]

    def execute(self, ctx) -> None:
        glue = boto3.client('glue')
        response = glue.start_job_run(
            JobName=self.job_name.value,
            Arguments=self.arguments.value or {}
        )
        self.job_run_id.value = response['JobRunId']


@xai_component
class GetGlueJobStatus(Component):
    """Component to get the status of an AWS Glue job run.

    ##### inPorts:
    - job_name (str): The name of the AWS Glue job.
    - job_run_id (str): The ID of the Glue job run.

    ##### outPorts:
    - job_status (str): The current status of the job run.
    """
    job_name: InArg[str]
    job_run_id: InArg[str]
    job_status: OutArg[str]

    def execute(self, ctx) -> None:
        glue = boto3.client('glue')
        response = glue.get_job_run(
            JobName=self.job_name.value,
            RunId=self.job_run_id.value
        )
        self.job_status.value = response['JobRun']['JobRunState']
