import boto3
from botocore.exceptions import ClientError

sns = boto3.resource('sns')

topic_arn = 'arn:aws:sns:us-east-2:123456789012:MyTopic'

topic = sns.topic(topic_arn)

attributes = {'some_key': 'coool'}

message = "Hello everyone!"


try:
    att_dict = {}
    for key, value in attributes.items():
        if isinstance(value, str):
            att_dict[key] = {'DataType': 'String', 'StringValue': value}
        elif isinstance(value, bytes):
            att_dict[key] = {'DataType': 'Binary', 'BinaryValue': value}

    response = topic.publish(Message=message, MessageAttributes=att_dict)
    message_id = response['MessageId']

except ClientError:
    print("Couldn't publish message to topic %s.", topic.arn)
else:
    print(f'Message published! message_id: {message_id}')
