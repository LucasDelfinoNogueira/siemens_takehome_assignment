from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
)
from constructs import Construct

class LambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, queue, topic, **kwargs):
        super().__init__(scope, id, **kwargs)

        fn = lambda_.Function(
            self, "LogAlertHandler",
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
