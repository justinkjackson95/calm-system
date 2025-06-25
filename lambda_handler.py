import json
import time

def lambda_handler(event, context):
    output = []

    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'].encode('utf-8'))
        speed = payload.get("speed", 0)

        # Filter out noise or speeds below 5 mph
        if speed >= 5:
            payload["processed_timestamp"] = time.time()
            output.append(payload)

    # TODO: Send to S3, DynamoDB, or another service
    print(f"Processed records: {len(output)}")
    return {"filtered": output}
