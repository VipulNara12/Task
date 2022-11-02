import boto3
from fastapi import FastAPI

app = FastAPI()
session = boto3.Session()
s3_client = session.client('s3')
s3_bucket_name = 'vipbucket'
object_name = 'birds/parrot.jpeg'


@app.get("/bucket_presign")
def file_download():
    """

    :rtype: object
    """
    response = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': s3_bucket_name,
            'Key': object_name
        },
        ExpiresIn=3600
    )
    return response



