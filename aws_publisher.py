import boto3
import json
from config import KINESIS_STREAM_NAME, AWS_REGION

kinesis = boto3.client("kinesis", region_name=AWS_REGION)

def publish_data(data):
    kinesis.put_record(
        StreamName=KINESIS_STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey="radar"
    )
