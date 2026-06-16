# Spark and SQL Learning Lab

## Project Overview

This repository is a hands-on learning project focused on developing practical Data Engineering skills using Python, SQLite, Pandas, and Apache Spark.

The primary goal is to understand how data moves between storage systems and processing frameworks while exploring fundamental and advanced concepts in SQL and Spark.

The project begins with a relational dataset stored in SQLite, loads data into Pandas for inspection, and then processes it using Apache Spark DataFrames.

---

## Learning Objectives

### Apache Spark

This project is designed to explore:

* SparkSession creation and configuration
* Spark DataFrames
* Narrow Transformations
* Wide Transformations
* Partitioning
* Shuffling
* Salting techniques
* Broadcast Variables
* Broadcast Joins
* Lazy Evaluation
* Catalyst Optimizer
* Physical and Logical Execution Plans
* Performance Optimization Techniques
* Common Spark Bottlenecks
* Spark Best Practices

### SQL

This project also serves as a SQL practice environment covering:

* Inner Joins
* Left Joins
* Right Joins
* Full Outer Joins
* Group By
* Aggregate Functions
* Window Functions
* Common Table Expressions (CTEs)
* Subqueries
* Indexes
* Query Optimization
* Execution Plans

---

## Current Workflow

```text

SQLite Database
   │
   ▼
Pandas DataFrame
   │
   ▼
Spark DataFrame
   │
   ▼
Transformations & Analysis
```

---

## Project Structure

```text
DATA_PIPELINE_PROJECT/

├── data/
│   ├── family.csv
│   ├── my_db.db
│   └── mydb.db
│
├── src/
│   ├── main.py
│   ├── spark_session.py
│   └── SQL_query.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── req_dev.txt
```

---

## Components

### spark_session.py

Responsible for:

* Creating SparkSession
* Configuring Spark environment
* Initializing Spark context

### SQL_query.py

Contains SQL queries used to:

* Retrieve data from SQLite
* Perform aggregations
* Test joins
* Practice advanced SQL concepts

### main.py

Acts as the project entry point and performs:

* SQLite connection
* Data extraction
* Pandas DataFrame creation
* Spark DataFrame creation
* Transformation execution
* Result visualization

---

## Concepts Demonstrated

### Data Ingestion

Data is extracted from SQLite and loaded into Pandas before being converted into Spark DataFrames.

### Narrow Transformations

Examples include:

* filter()
* select()
* withColumn()

These transformations do not require data movement between partitions.

### Wide Transformations

Examples include:

* groupBy()
* join()
* distinct()

These operations trigger shuffling across the cluster.

### Query Plan Analysis

Spark's `explain()` function is used to understand:

* Logical Plan
* Optimized Logical Plan
* Physical Plan

### SQL Performance Analysis

The project explores:

* Index creation
* Query execution plans
* Optimization strategies

---

## Technologies Used

* Python
* Pandas
* SQLite
* Apache Spark (PySpark)
* SQL
* Git
* GitHub

---

## Future Enhancements

Planned additions include:

* Partitioning demonstrations
* Broadcast join examples
* Salting implementation for skewed data
* Spark caching and persistence
* Data skew analysis
* Spark performance benchmarking
* Airflow orchestration
* Docker containerization
* Cloud deployment

---

## Learning Outcome

This repository documents my journey of learning Data Engineering concepts with a strong focus on:

* SQL Query Optimization
* Distributed Data Processing
* Spark Internals
* Performance Tuning
* Data Transformation Techniques

The objective is to build a solid foundation for developing production-grade data pipelines and scalable data platforms.

---

## Author

Ankit Dutta
Data Engineer
