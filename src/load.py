import logging
from botocore.exceptions import ClientError
import boto3
import os


def upload_file(file_name, bucket, object_name=None) -> bool:
    '''
    Function that uploads data to s3 bucket on AWS
    :param file_name:
    :param bucket:
    :param object_name:
    :return:
    '''
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
