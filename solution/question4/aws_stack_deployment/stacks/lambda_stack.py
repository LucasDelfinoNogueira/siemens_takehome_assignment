"""
lambda_stack.py: CDK stack for deploying a Lambda function triggered by an SQS queue.

This stack configures an AWS Lambda function that listens to SQS messages and publishes alerts to an SNS topic.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
    aws_sqs as sqs,
    aws_sns as sns,
)
from constructs import Construct
from typing import Any


class LambdaStack(Stack):
    """
    CDK stack that defines a Lambda function which:
    - Is triggered by messages in an SQS queue
    - Publishes alerts to an SNS topic
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        queue: sqs.IQueue,
        topic: sns.ITopic,
        **kwargs: Any
    ) -> None:
        """
        Initialize the LambdaStack.

        Args:
            scope (Construct): The scope in which to define this construct.
            id (str): Identifier for this stack.
            queue (sqs.IQueue): The SQS queue to trigger the Lambda.
            topic (sns.ITopic): The SNS topic the Lambda will publish to.
            **kwargs (Any): Additional keyword arguments passed to the Stack.
        """
        super().__init__(scope, id, **kwargs)

        fn = lambda_.Function(
            self,
            "LogAlertHandler",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="alert_handler.main",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TOPIC_ARN": topic.topic_arn
            }
        )

        fn.add_event_source(lambda_event_sources.SqsEventSource(queue))

        topic.grant_publish(fn)
        queue.grant_consume_messages(fn)
