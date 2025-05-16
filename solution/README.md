# Data Homework Solutions

This repository contains Python code and documentation for the DISW take-home data engineering assignment.

---

## 📁 Repository Structure

```
records.json               # Sample input data
solution/
├── requirements.txt       # Python dependencies
├── README.md              # General documentation (this file)
├── question1/             # Solution for finding 3 closest logins to a target date
├── question2/             # Solution for finding 2 closest logins between users
├── question3/             # Stream-processing design explanation
└── question4/             # Event-driven alerting system on AWS (CDK + Lambda + SQS + SNS)
```

---

## 🛠️ Setup Instructions

1. Make sure you have **Python 3.9 or higher** installed.
2. Install required dependencies:

```bash
pip install -r solution/requirements.txt
```

---

## 📌 Questions Summary

### ✅ Question 1: Closest Logins to a Specific Timestamp

> Find the 3 users whose login times are closest to `2025-02-01 00:00 UTC`.

📂 [See solution and explanation](solution/question1/README.md)

---

### ✅ Question 2: Closest Login Pair

> Identify the 2 users whose login times are closest together.

📂 [See solution and explanation](solution/question2/README.md)

---

### ✅ Question 3: Design for High-Volume Streams

> Describe how to approach the same login problem if analyzing 1 million+ streaming records.

📂 [See solution and explanation](solution/question3/README.md)

---

### ✅ Question 4: Event-Driven AWS Log Alerting System

> Build an event-driven log monitoring system using:
- Python log producer
- AWS SQS for ingestion
- AWS Lambda for processing
- AWS SNS for alerting
- AWS CDK (Python) for Infrastructure as Code

📂 [See solution and explanation](solution/question4/README.md)

---