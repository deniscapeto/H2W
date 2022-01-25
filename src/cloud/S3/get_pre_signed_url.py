import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3', region_name='us-east-1')

bucket_name = 'mywebsitebucket-testedenis'

object_key = 'randomKey'

try:
    response = s3.meta.client.generate_presigned_post(
        Bucket=bucket_name,
        Key=object_key,
        # ExpiresIn=expires_in
    )
    print(f'Got presigned POST URL: {response["url"]}')

except ClientError:
    print(
        f"Couldn't get a presigned POST URL for bucket '{bucket_name}' "
        "and object '{object_key}'"
    )
