import pandas as pd
import boto3
import s3fs
from io import StringIO

#define global variable
queue_url = 'https://sqs.us-west-2.amazonaws.com/761400977934/swaram92-test-q'

#create clients
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')

if __name__ == "__main__":
    #Collecting queue message one by one until queue is empty
    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
