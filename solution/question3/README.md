# Question 3: Streaming 1 Million Records

**Task Recap:**  
Find the 3 users whose `last_login` timestamps are closest (in absolute terms) to `2025-02-01 00:00 UTC` — across a stream of 1 million records.

---

## Option 1: In-Memory Distributed Processing

**Approach:**

- Use PySpark to load and process the 1M records in parallel
- Parse `last_login` using `to_timestamp()`
- Compute absolute time difference from the target date
- Use `orderBy` on the computed diff
- Select the top 3 records with `.limit(3)`

**Why Use It:**

- Distributed in-memory processing makes it scalable  
- PySpark handles large datasets efficiently with minimal code  
- Integrates well with streaming tools like Kafka or Kinesis

**Best When:**

- You're working in a Spark ecosystem (e.g. Databricks, EMR, Glue)  
- The dataset is too large for pandas or local memory


---

## Option 2: Read Batches

**Approach:**

- Process the stream in chunks (100k at a time)
- For each chunk:
  - Parse timestamps and compute diffs
  - Keep only the top 3 closest records
- After all batches:
  - Combine all intermediate top-3s
  - Run final top-3 selection

**Why Use It:**

- Avoids loading all 1M records in memory  
- Straightforward implementation with batching

**Best When:**

- You're limited by memory but can handle disk or batch processing

---

## Option 3: Time-Series Database or Search Engine

**Approach:**

- Index `last_login` in a time-series database like Elasticsearch
- Use a range or nearest-neighbor query around the target timestamp

**Why Use It:**

- Optimized for temporal queries  
- Scales well for millions to billions of records  
- Handles indexing, sorting, and query optimization internally

**Best When:**

- You have infrastructure for large-scale data indexing  
- The solution will be reused or productionized

---

## Option 4: Real-Time Stream Processing with Apache Flink

**Approach:**

- Use Apache Flink to consume the data stream directly (from Kafka for example)
- Define a processing pipeline:
  - Parse and normalize `last_login`
  - Compute absolute time difference
  - Use a keyed process function or custom operator to maintain the top 3 closest records in state
- Emit updated results as the stream progresses

**Why Use It:**

- Built for true low-latency, high-throughput stream processing  
- Scales horizontally

**Best When:**

- You need real-time computation over unbounded data  
- You already use Flink or need complex event-driven pipelines  
- Low latency and stream-native architecture are required
