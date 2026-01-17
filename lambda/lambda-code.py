import json
import boto3
import urllib.parse
import os

s3 = boto3.client('s3')
DEST_BUCKET = "my-processed-bucket"

def lambda_handler(event, context):
    function_name = context.function_name

    for record in event['Records']:
        body = json.loads(record['body'])
        message = json.loads(body['Message'])

        bucket = message['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(
            message['Records'][0]['s3']['object']['key']
        )

        s3.copy_object(
            CopySource={'Bucket': bucket, 'Key': key},
            Bucket=DEST_BUCKET,
            Key=f"processed/{function_name}/{key}"
        )

        print(f"{function_name} processed {key}")

    return {"status": "success"}
