import boto3
import json
import time
import random
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), 'secrets.env')
load_dotenv(dotenv_path=env_path)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
QUEUE_NAME = os.getenv("QUEUE_NAME")

QUEUE_URL = f"https://sqs.{AWS_REGION}.amazonaws.com/{AWS_ACCOUNT_ID}/{QUEUE_NAME}"


# Setup SQS Boto3 client
sqs = boto3.client(
    'sqs',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Define Mock messages
MESSAGES = [
    "INFO: Application started successfully.",
    "WARNING: Disk usage at 85%.",
    "ERROR: Database connection failed."
    "INFO: Scheduled job completed."
]

def send_log():
    message = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": random.choice(MESSAGES)
    }
    print(f'[DEBUG] The SQS Queue URL is: {QUEUE_URL}')
    sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(message))
    print(f"Sent: {message}")

if __name__ == '__main__':
    # Send event every 30 seconds. Need a KeyboardInterrupt to stop running.
    while True:
        send_log()
        time.sleep(30)
