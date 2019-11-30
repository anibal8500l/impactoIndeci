import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 's3-str-bucket' # nombre del bucket S3
KEY = '5E0.gif' # nombre del archivo

object_name = KEY

s3_client = boto3.client('s3')
try:
    response = s3_client.upload_file(KEY, BUCKET_NAME, object_name)
except ClientError as e:
    print("The object does not exist.")
