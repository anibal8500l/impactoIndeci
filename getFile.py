import boto3
import botocore

BUCKET_NAME = 's3-str-bucket' # nombre del bucket S3
KEY = '5E0.gif' # nombre del archivo

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, '5E0.gif')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
	raise
