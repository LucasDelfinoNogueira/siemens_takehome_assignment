# Question 1 Solutions

**Task:**  
Find the IDs of 3 users whose `last_login` timestamps are closest to `2025-02-01 00:00 UTC`.

---

## Approach 1a: Standard Python

**Steps:**

- Use `json` and `datetime`
- Load all records
- Compute time difference
- Sort by difference
- Select the top 3

**Pros:**

- Only uses Python’s built-in libraries
- Simple loop-based processing
- No external dependencies
- Minimal memory usage

**Cons:**

- Slower with millions of records

**Best when:**

- Processing small or infrequent jobs  
- Avoiding extra dependencies  
- Running in constrained environments (e.g. AWS Lambda, minimal containers)

---

## Approach 1b: Pandas DataFrame

**Steps:**

- Read JSON into a pandas DataFrame
- Parse `last_login` as datetime
- Compute the difference from the target timestamp
- Use `nsmallest()` to select the closest 3

**Pros:**

- Efficient with large datasets  
- Vectorized datetime operations  
- Faster and more concise for bulk operations

**Cons:**

- Higher memory usage  
- Requires the pandas library

**Best when:**

- Processing thousands to millions of rows  
- pandas is already part of your stack  
- Speed and expressiveness are priorities

---

## How to Run

```bash
python main_1a.py
python main_1b.py
```