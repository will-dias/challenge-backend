from odmantic import ObjectId

from src.aws.client import get_aws_client

s3_client = get_aws_client('s3')


def get_object(bucket_name: str, key: ObjectId) -> bytes:
    response = s3_client.get_object(Bucket=bucket_name, Key=str(key))
    return response['Body'].read().decode('utf-8')
