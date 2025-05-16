"""
sns_stack.py: CDK stack for creating an SNS topic and subscribing email addresses.

This stack provisions an SNS topic and adds each provided email address as a subscription.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

from aws_cdk import (
    Stack,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions
)
from constructs import Construct
from typing import List, Any


class SNSStack(Stack):
    """
    CDK stack to define an SNS topic and subscribe a list of email addresses.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        email_list: List[str],
        **kwargs: Any
    ) -> None:
        """
        Initialize the SNSStack.

        Args:
            scope (Construct): The scope in which to define this construct.
            id (str): Identifier for this stack.
            email_list (List[str]): List of email addresses to subscribe to the topic.
            **kwargs (Any): Additional keyword arguments passed to the Stack.
        """
        super().__init__(scope, id, **kwargs)

        self.topic = sns.Topic(self, "LogAlertsTopic")

        for email in email_list:
            self.topic.add_subscription(
                subscriptions.EmailSubscription(email.strip())
            )
