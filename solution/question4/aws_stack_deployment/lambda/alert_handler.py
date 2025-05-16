import json
import os
import boto3

sns = boto3.client("sns")
TOPIC_ARN = os.environ["TOPIC_ARN"]

def main(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        message = body.get("message", "")

        # Print Alert message for logging in Cloudwatch
        alert_msg = f"ALERT: {message}"
        print(alert_msg)
        
        if "ERROR" in message or "WARNING" in message:
            sns.publish(
                TopicArn=TOPIC_ARN,
                Message=alert_msg,
                Subject="Log Alert"
            )
