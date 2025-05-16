# AWS Log Analysis and Alerting System

This project simulates a real-time log analysis and alerting system using AWS services. It includes:

- Log generation using a Python script
- Real-time ingestion via SQS
- Processing using an AWS Lambda function
- Notification via SNS email alerts
- Full infrastructure as code using AWS CDK (Python)

---

## 📁 Project Structure

```
DATA_HOMEWORK-2/
└── solution/
    └── question4/
        ├── aws_stack_deployment/   # CDK infrastructure code
        │   ├── app.py
        │   └── stacks/
        │       ├── sqs_stack.py
        │       ├── sns_stack.py
        │       └── lambda_stack.py
        ├── lambda/
        │   └── alert_handler.py     # Lambda function logic
        ├── log_producer.py          # Python script to send logs
        ├── secrets.env              # Environment variables
        ├── requirements.txt
        └── README.md
```

---

## 🛠️ Stack Overview (CDK)

### 1. **SQS Queue**
- Collects log messages from the producer script.
- Created in `sqs_stack.py`.

### 2. **SNS Topic**
- Sends email alerts when triggered by Lambda.
- Includes multiple email subscriptions from `secrets.env`.
- Defined in `sns_stack.py`.

### 3. **Lambda Function**
- Triggered by messages arriving in SQS.
- Checks if log contains `ERROR` or `WARNING`.
- If so, sends alert to SNS.
- Defined in `lambda_stack.py`, code in `lambda/alert_handler.py`.

---

## 🔐 Environment Variables

Create a file called `secrets.env` in the same folder as `log_producer.py` (./question4/secrets.env):

```env
AWS_REGION=us-west-1
AWS_ACCOUNT_ID=YOUR_ACCOUNT_ID
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY

QUEUE_NAME=log-alerting-queue
ALERT_EMAILS=you@example.com,user2@example.com
```

> ⚠️ This file is loaded by both the CDK app and the log producer. It should never be committed — make sure it is listed in `.gitignore`.

---

## ✅ Installation

1. Clone the project
2. CD to ./question4/ if you haven't
2. Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install AWS CDK CLI:

```bash
npm install -g aws-cdk
```

---

## 🚀 Deploying the Infrastructure

1. Load the credentials from your `.env`:

```bash
export $(grep -v '^#' secrets.env | xargs)
```

> ⚠️ Make sure your secrets.env file is already populated with the correct values.

2. Bootstrap the CDK environment (only needed once per account/region):

```bash
cd aws_stack_deployment
cdk bootstrap
```

3. Deploy the stack:

```bash
cdk deploy --all
```

---

## 🧪 Testing the System

### Run the log producer script:

```bash
python log_producer.py
```

Each execution will send a log message to the SQS queue. If the message contains `"ERROR"` or `"WARNING"`, it will:

- Trigger the Lambda
- Publish an alert to SNS
- Send email to all email addresses listed in `ALERT_EMAILS`

---

## 📜 Lambda Logic

`lambda/alert_handler.py`:

- Triggered by SQS
- Parses each message
- Looks for `"ERROR"` or `"WARNING"` in the `"message"` field
- Sends alert to SNS if found
- Otherwise just print the message

---

## 🧹 Cleaning Up (Avoid Charges)

1. Destroy the deployed stacks:

```bash
cd aws_stack_deployment
cdk destroy --all
```

2. Delete the CDK bootstrap stack and roles:

```bash
cdk destroy CDKToolkit
```

3. Deactivate the virtual environment:

```bash
deactivate
```

---

## 📦 Dependencies

### Python packages (`requirements.txt`)

```
aws-cdk-lib==2.130.0
constructs>=10.0.0,<11.0.0
boto3
python-dotenv
```

Install them with:

```bash
pip install -r requirements.txt
```

### Node packages

- AWS CDK CLI (`npm install -g aws-cdk`)
- Node.js version **20.x** recommended

---

## 📘 Additional Notes

- The Lambda function uses inline permissions to consume SQS and publish to SNS.
- Email subscriptions require confirmation before receiving alerts.

---

## ✅ Verified AWS Resources Created

- ✅ 1 SQS Queue  
- ✅ 1 SNS Topic + Email Subscriptions  
- ✅ 1 Lambda Function  
- ✅ IAM roles (I have not found a way of destroying those Roles using the ```cdk destroy```)
