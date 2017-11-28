from uuid import uuid4
import boto3
import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename


def s3_upload(source_file, upload_dir=None, acl='public-read'):
    """ Uploads File Object to Amazon S3


        Also generates a unique filename via
        the uuid4 function combined with the file extension from
        the source file.
    """

    source_filename = secure_filename(source_file.filename)
    source_extension = os.path.splitext(source_filename)[1]

    destination_filename = uuid4().hex + source_extension

    # Connect to S3 and upload file.
    s3 = boto3.client('s3')
    bucket_name = "application-resumes"
    s3.upload_fileobj(source_file, bucket_name, destination_filename)

    return destination_filename
