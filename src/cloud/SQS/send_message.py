import boto3

# Create SQS client
client = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/1234/example-teste'
queue_url = 'https://sqs.us-east-1.amazonaws.com/193923156883/KeyLogs'

response = client.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello! This is my message',
    DelaySeconds=123
)

print(response)
