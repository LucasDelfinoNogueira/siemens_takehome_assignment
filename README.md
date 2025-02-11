# DISW Take-Home Assignment #

**PURPOSE:** 

Upload code answers for this data engineering interviews.

*INSTRUCTIONS ON HOW TO USE THIS REPO:** 

Clone this repo & upload your answers to Questions 1-3 in any 3rd party code repository like Github, Bitbubucket, or Gitlab. When you answered the questions in your repo, please send us a link to the repo for us to review.

You can develop your code in your language of choice, though most of the data team uses Python.


## Question 1 (code required): 
You have two arrays of integers.
```
a = [47,24,95,184,13,3,12,18]
b = [83,9,32,29,52,90,108,14]
```

Provide 2 or 3 different ways to calculate the pair of values (one value in each array) with the smallest non-negative difference.

Return the elements in the array and the smallest non-negative difference.

For example, the answer with array `a` & `b` above is `b = 14` and `a = 13` because their difference is `14-13 = 1`, which is the smallest non-negative difference. As a note, an element in array `a` can be subtracted from an element in array `b` and vice versa.

We are not looking for the most optimal code, but a variety of methods you could use calculate the smallest different and why you would select one method over another.

## Question 2 (code required):
Create 2 arrays of random integers between 1 and 10,000,000. Each array should be 1,000 integers long. 

Apply the multiple methods you derived in Question 1 with the 2 new arrays of integers you calculate in this question. 

Which algorithm performed best? Which algorithm performed worst? And why? What is the Big0 notation for each of your methods?


## Question 3 (no code required. We're only looking for a written response):
Conceptually, what are the different tools such as code libraries or infrastructure that could help you 
find the smallest non-negative difference between 1 million lists that are 5,000 integers long?

## Question 4 (Optional - may require AWS Free Tier account)
### Log Analysis and Alerting

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





