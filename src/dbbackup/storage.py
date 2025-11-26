import os
import logging
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

logger = logging.getLogger("dbbackup")

def upload_to_storage(filepath, cfg):
    provider = cfg["storage"]["provider"]

    if provider == "s3":
        return upload_to_s3(filepath, cfg)

    raise ValueError(f"Unsupported storage provider: {provider}")

def upload_to_s3(filepath, cfg):
    bucket = cfg["storage"]["bucket"]
    key = os.path.basename(filepath)

    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=cfg["storage"]["aws_access_key"],
            aws_secret_access_key=cfg["storage"]["aws_secret_key"],
        )

        s3.upload_file(filepath, bucket, key)
        logger.info(f"Uploaded to S3: s3://{bucket}/{key}")

    except (BotoCoreError, NoCredentialsError) as e:
        logger.error(f"S3 upload failed: {e}")

