"""
sqs_stack.py: CDK stack for creating an SQS queue with a configurable name and visibility timeout.

This stack provisions an AWS SQS queue for use in log alerting systems.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import os
from aws_cdk import Stack, Duration, aws_sqs as sqs
from constructs import Construct
from dotenv import load_dotenv
from typing import Any

# Load secrets.env from two levels up
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'secrets.env'))
load_dotenv(dotenv_path=env_path, override=True)

class SQSStack(Stack):
    """
    CDK stack that creates an SQS queue for handling log messages.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs: Any
    ) -> None:
        """
        Initialize the SQSStack.

        Args:
            scope (Construct): The scope in which this stack is defined.
            id (str): Identifier for this stack.
            **kwargs (Any): Additional keyword arguments passed to the Stack.
        """
        super().__init__(scope, id, **kwargs)

        # Get Queue name from env variables
        queue_name = os.getenv("QUEUE_NAME", "log-alerting-queue")

        self.queue = sqs.Queue(
            self,
            "LogQueue",
            queue_name=queue_name,
            visibility_timeout=Duration.seconds(60)
        )
