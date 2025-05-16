from aws_cdk import Stack, aws_sns as sns, aws_sns_subscriptions as subscriptions
from constructs import Construct

class SNSStack(Stack):
    def __init__(self, scope: Construct, id: str, email_list: list[str], **kwargs):
        super().__init__(scope, id, **kwargs)

        self.topic = sns.Topic(self, "LogAlertsTopic")

        for email in email_list:
            self.topic.add_subscription(subscriptions.EmailSubscription(email.strip()))
