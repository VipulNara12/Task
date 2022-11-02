import boto3
from fastapi import FastAPI

app = FastAPI()


@app.get("/bucket_display")
def get_data():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        l1 = bucket.name
        my_bucket = s3.Bucket(bucket.name)
        for file in my_bucket.objects.all():
            l2 = file.key
    return {l1: {l2}}


