"""
app.py: Main CDK application entry point.

This script loads environment variables, sets up AWS credentials and region,
and deploys the SQS, SNS, and Lambda stacks.
"""

__owner__ = "Lucas Delfino"
__created_at__ = "2025-05-16"
__updated_at__ = "2025-05-16"

import os
import aws_cdk as cdk
from dotenv import load_dotenv

from stacks.sqs_stack import SQSStack
from stacks.sns_stack import SNSStack
from stacks.lambda_stack import LambdaStack

# Load environment variables from secrets.env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'secrets.env'))
load_dotenv(dotenv_path=env_path)

# Export credentials to environment for AWS SDK to use
os.environ["AWS_ACCESS_KEY_ID"] = os.getenv("AWS_ACCESS_KEY_ID")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv("AWS_SECRET_ACCESS_KEY")
os.environ["AWS_REGION"] = os.getenv("AWS_REGION")

# Set deployment configuration
account = os.getenv("AWS_ACCOUNT_ID")
region = os.getenv("AWS_REGION", "us-east-1")
email_list = os.getenv("ALERT_EMAILS", "").split(",")

# Set CDK deployment environment
env = cdk.Environment(account=account, region=region)

# Initialize CDK app
app = cdk.App()

# Deploy stacks
sqs_stack = SQSStack(app, "SQSStack", env=env)
sns_stack = SNSStack(app, "SNSStack", email_list=email_list, env=env)
lambda_stack = LambdaStack(app, "LambdaStack", queue=sqs_stack.queue, topic=sns_stack.topic, env=env)

# Synthesize app
app.synth()
