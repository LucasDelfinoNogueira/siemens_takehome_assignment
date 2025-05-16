import os
from aws_cdk import Stack, Duration, aws_sqs as sqs
from constructs import Construct
from dotenv import load_dotenv

# Load secrets.env from one level up
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'secrets.env'))
load_dotenv(dotenv_path=env_path, override=True)

class SQSStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Get Queue name from env variables
        queue_name = os.getenv("QUEUE_NAME", "log-alerting-queue")

        self.queue = sqs.Queue(
            self,
            "LogQueue",
            queue_name=queue_name,
            visibility_timeout=Duration.seconds(60)
        )
