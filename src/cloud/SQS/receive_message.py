import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.sa-east-1.amazonaws.com/1234/example-teste.fifo'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,  # Maximum message count
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=5,
    WaitTimeSeconds=0  # polling duration
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

print(message)

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)
