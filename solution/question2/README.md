# Question 2 Solutions

**Task:**  
Find the 2 users whose `last_login` timestamps are closest to each other.

---

## Approach 2a: Standard Python

**Steps:**

- Use `json` and `datetime`
- Load records from a hardcoded file path
- Parse all login timestamps
- Sort them chronologically
- Compare adjacent timestamps to find the smallest gap

**Pros:**

- Pure Python (no external libraries)
- Low memory usage
- Easy to run in constrained environments

**Cons:**

- Slower for large datasets  
- Manual time difference calculation  
- More verbouse code

**Best when:**

- Dataset is small or medium-sized  
- Simplicity and zero dependencies are required  
- Running in restricted environments like AWS Lambda

---

## Approach 2b: Pandas DataFrame

**Steps:**

- Load JSON data into a pandas DataFrame  
- Parse and sort `last_login` timestamps  
- Compute time differences using `diff()`  
- Find the smallest non-null difference  
- Return the corresponding two rows

**Pros:**

- Fast and efficient on large datasets  
- Uses vectorized operations  
- Minimal code for complex logic

**Cons:**

- Requires the pandas library  
- Higher memory consumption

**Best when:**

- Working with thousands or millions of records  
- Already using pandas in the project  
- Prioritizing speed and code conciseness

---

## How to Run

```bash
python main_2a.py
python main_2b.py
```