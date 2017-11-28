import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename


def s3_upload(source_file):
    """ Uploads File Object to Amazon S3

        Given a File Object, this function should upload the file to the S3 bucket that you created earlier,
        and return the name of the uploaded file.

        It's common practice to replace original filenames with a completely random new filename when storing on the server,
        and we want to do the same. This way, we don't have to worry about duplicate filenames (chance of a collision is negligible) and can serve the files 
        via URL without exposing any client information.

        You can run the server with the following terminal command:
        $ python app.py
        The server will run on port 5000 and you can access it through the EC2 instance's public DNS.
    """

    source_filename = secure_filename(source_file.filename)
    source_extension = os.path.splitext(source_filename)[1]

    # create a destination filename that is random and includes the original extension
    # e.g. "AndrewChansResume.pdf" becomes "Jnisui278aJbhfqewiua.pdf"
    # Hint: uuid may be useful. Check out the examples at https://docs.python.org/2/library/uuid.html
    #=================
    destination_filename = #***YOUR CODE HERE***#
    #=================
    # Connect to S3 and upload file.
    # You should use boto3. Check the boto3 documentation for a file upload function that upload File Objects instead of filenames.
    # http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.upload_file
    #=================
    # YOUR CODE HERE
    #=================

    return destination_filename
