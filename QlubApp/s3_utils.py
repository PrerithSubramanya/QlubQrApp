import boto3
from botocore.client import BaseClient


def get_s3_client() -> BaseClient:
    return boto3.client(
        service_name="s3",
        region_name="ap-southeast-1",
        aws_access_key_id="AKIATXT7JADPJAJYLKBO",
        aws_secret_access_key="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",
    )


def get_s3_resource() -> boto3.resource:
    return boto3.resource(
        service_name="s3",
        region_name="ap-southeast-1",
        aws_access_key_id="AKIATXT7JADPJAJYLKBO",
        aws_secret_access_key="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",
    )


def get_table_qr_image(table_name: str) -> str:
    s3 = get_s3_client()
    return s3.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": "qlubqrapp",
            "Key": table_name,
        },
        ExpiresIn=3600,
    )
