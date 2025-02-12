# DISW Take-Home Assignment #

## Purpose

Upload code answers for this data engineering interviews.

## Instructions on how to use this repo:

Clone this repo & upload your answers to Questions 1-3 in any 3rd party code repository like Github, Bitbubucket, or Gitlab. When you have answered the questions in your repo, please send us a link to the repo for us to review.

You can develop your code in your language of choice, though most of the data team uses Python.

For the first 3 questions, use the included file `records.json`. It contains 100 records with an email address (treated as an account name), a user ID, and a date of last login as UTC. Example:

```
  {
    "name": "peru-lengthwise-attic@example.com",
    "id": "32e50cd2-2873-41d5-a721-493b57d6c4e7",
    "last_login": "2025-01-10T19:41:24Z"
  }
```

### Question 1 (code required): 
Write a small application to print out the IDs of the 3 users with logins closest to 2025-02-01 00:00 UTC.

We are not looking for the most optimal code, but a variety of methods you could use calculate the smallest difference and why you would select one method over another.

### Question 2 (code required): 
Write a small application to print out the IDs of the 2 users who logged in at the closest time to each other, along with the times of login.

Again, we are not looking for the most optimal code, but a variety of plausible approaches.

### Question 3. (code not required):
Describe how you might approach question 1 if you are examining a stream of 1 million records instead.

### Question 4 (Optional - may require AWS Free Tier account)

#### Log Analysis and Alerting

This assignment tests your AWS and Python data engineering skills by building a simplified log analysis and alerting system.

**Scenario:**

You have a single application generating logs.  You need to monitor these logs for specific error messages and trigger alerts when they occur.

**Requirements:**

1. **Log Ingestion:**  Simulate a log stream (e.g., a Python script generating log entries).  Each log entry should be a JSON string with a "message" field.

2. **Real-time Processing:** Use AWS Lambda to process these log entries in real-time.  The Lambda function should:
    * Parse the JSON log entry.
    * Check if the "message" field contains a specific error string (e.g., "ERROR_CODE_123").

3. **Alerting:** If the error string is found, trigger an alert.  For simplicity, just print a message to the console (CloudWatch Logs) indicating an alert has been triggered.  You don't need to integrate with an external alerting service.

4. **Infrastructure as Code:**  Use the AWS CDK (Python) to define the Lambda function and any necessary supporting resources (e.g., an SQS queue if you want to decouple ingestion and processing, though this is optional for the simplified version).

5. **Testing:** Provide a script to generate sample log entries and demonstrate how to trigger the alert.

6. **Documentation:** Include a README explaining your design and how to run the test script.

**Simplified Example Log Entry:**

{"message": "Application started successfully."}