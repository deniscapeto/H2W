import boto3

import os
cwd = os.getcwd()


if __name__ == '__main__':

    # AWS VARIABLES MUST BE ALREADY CONFIGURED
    s3_client = boto3.client('s3')
    print(cwd)
    with open("src/cloud/s3.py", "rb") as f:
        s3_client.upload_fileobj(f, "mywebsitebucket-testedenis", "s3_obj.py")
