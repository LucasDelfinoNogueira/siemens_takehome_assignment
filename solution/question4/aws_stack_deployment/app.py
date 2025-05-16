import aws_cdk as cdk
from stacks.sqs_stack import SQSStack
from stacks.sns_stack import SNSStack
from stacks.lambda_stack import LambdaStack
from dotenv import load_dotenv
import os

# Load secrets
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'secrets.env'))
load_dotenv(dotenv_path=env_path)

# Export credentials to environment for AWS SDK to use
os.environ["AWS_ACCESS_KEY_ID"] = os.getenv("AWS_ACCESS_KEY_ID")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv("AWS_SECRET_ACCESS_KEY")
os.environ["AWS_REGION"] = os.getenv("AWS_REGION")

account = os.getenv("AWS_ACCOUNT_ID")
region = os.getenv("AWS_REGION", "us-east-1")
email_list = os.getenv("ALERT_EMAILS", "").split(",")

# Set CDK deployment environment
env = cdk.Environment(account=account, region=region)

app = cdk.App()

sqs_stack = SQSStack(app, "SQSStack", env=env)
sns_stack = SNSStack(app, "SNSStack", email_list=email_list, env=env)
lambda_stack = LambdaStack(app, "LambdaStack", queue=sqs_stack.queue, topic=sns_stack.topic, env=env)

app.synth()
