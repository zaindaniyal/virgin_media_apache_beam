# Apache Beam Pipeline

This is an Apache Beam pipeline that processes transactions data to filter and summarise transactions based on specific criteria.

## Overview

The Apache Beam pipeline reads transaction data from a CSV file, applies filters and transformations, and writes the processed data to a JSONL file. The pipeline uses Apache Beam's data processing capabilities and can be run on various execution engines, such as Apache Flink, Apache Spark, or Google Cloud Dataflow.

The pipeline performs the following steps:

1. **Data Reading**: The pipeline reads transaction data from a CSV file, serving as the input source for subsequent transformations.

2. **Filtering and Mapping**: Transactions are filtered and transformed based on specified criteria. The pipeline selects specific transactions and maps them into key-value pairs, extracting relevant information for further processing.

3. **Combining and Summarising**: The pipeline combines transactions by date and calculates the sum of transaction amounts. This step aggregates the data, providing a consolidated view of the total transaction amount for each date.

4. **JSON Formatting**: The pipeline formats the aggregated data into JSON objects. Each object represents a summarised transaction, containing the date and the corresponding sum of transaction amounts. The JSON format facilitates easy data manipulation and analysis.

5. **Output Generation**: The pipeline writes the formatted JSON objects to a compressed JSONL (JSON Lines) file. This output file stores the summarised transaction data in a compressed format, ensuring efficient storage and enabling further analysis or data exchange.

By leveraging Apache Beam's capabilities, this pipeline ensures efficient and scalable processing of transaction data while providing flexibility to run on different execution engines, such as Apache Flink, Apache Spark, or Google Cloud Dataflow.

# File Descriptions

The project consists of three main Python scripts:

1. **main.py**: This is the primary script that sets up and runs the Apache Beam pipeline. It includes two classes, `FilterAndSumFn` and `ProcessTransactions`, and a main `run` function. The `FilterAndSumFn` class is a custom DoFn (short for "Do Function") in Apache Beam's model, which processes and filters the transactions. The `ProcessTransactions` class is a custom PTransform (short for "Parallel Transform"), which is used to transform the transaction data. The `run` function sets up and runs the Apache Beam pipeline, reading the transaction data, processing it, and writing the results to a .jsonl.gz file.

2. **download.py**: This script contains the `download_public_file` function, which downloads a file from a given URL and saves it to the specified destination. This function is used to download the transaction data file from a Google Cloud Storage (GCS) bucket. It uses the `requests` library to make the HTTP GET request.

3. **tests.py**: This script contains two unit tests for the `ProcessTransactions` transform: `test_process_transactions_pass` and `test_process_transactions_fail`. The `test_process_transactions_pass` test checks that the `ProcessTransactions` transform correctly processes and transforms valid input data. The `test_process_transactions_fail` test checks that the `ProcessTransactions` transform correctly handles input data that does not meet the filtering criteria and outputs an empty PCollection. These tests are written using the `unittest` and `apache_beam.testing` libraries.

Each of these files plays a crucial role in the pipeline and helps ensure that the data processing is done accurately and reliably.

# main.py Overview

The provided Python script comprises three primary components:

1. **FilterAndSumFn(beam.DoFn)**: This class is a custom `DoFn` (short for "Do Function") in Apache Beam's model. It serves to process each element of the input data.

    In our specific case, the `FilterAndSumFn` processes transaction data received in the form of CSV strings. It filters transactions based on a condition (transaction year >= 2010 and transaction amount > 20). When these conditions are met, the function outputs a tuple of `(date, transaction_amount)`. If these conditions are not met, the function returns an empty list and the data point is dropped from the pipeline.

2. **ProcessTransactions(beam.PTransform)**: This class is a custom `PTransform` (short for "Parallel Transform"), which is used to transform one or more PCollections (the Apache Beam term for a dataset). 

    The `ProcessTransactions` PTransform processes the input PCollection by applying the `FilterAndSumFn` DoFn, summing the transactions by date, formatting the output into a JSON-like string, and writing the results to a .jsonl.gz file. The filename includes a timestamp for uniqueness. 

3. **run()**: This function sets up and runs the Apache Beam pipeline. It reads transaction data from a Google Cloud Storage (GCS) bucket, applies the `ProcessTransactions` PTransform to the input data, and writes the processed data to a .jsonl.gz file.

## Use Cases

This Apache Beam pipeline can be leveraged for efficient data processing in cases where large volumes of transaction data need to be filtered, aggregated, and summarised. It can be applied in areas like retail sales analysis, financial transaction monitoring, and IoT data processing. The pipeline's ability to output to a JSONL file makes the resulting data convenient for subsequent analysis, machine learning, and visualization.

Here are some simplified scenarios where Apache Beam streaming pipelines can be put to use:

1. **Real-Time Fraud Detection:** Detect fraudulent activities in financial transactions as they occur.
2. **Live Social Media Analysis:** Monitor and analyse social media posts or comments in real-time, identifying trending topics or real-time sentiment about a brand or product.
3. **E-commerce Personalisation:** Keep track of a user's live activity on an e-commerce platform, updating product recommendations based on their activity.
4. **Health Monitoring:** Process live data from wearable devices, sending alerts to healthcare providers on critical changes in a patient's health status.
5. **Traffic Monitoring:** Analyse real-time data from GPS and traffic systems, providing live traffic updates and suggestions for re-routing to drivers.
6. **Network Security:** Monitor network traffic in real-time to identify potential security threats or breaches.
7. **Supply Chain Management:** Oversee live data from various points in a supply chain, assisting in identifying and addressing potential issues quickly.
8. **Customer Support:** Evaluate incoming customer support requests in real-time, helping to prioritize and assign them effectively.
9. **Smart Homes:** Process live data from various devices and sensors in a smart home, automating tasks and improving efficiency.
10. **Live Event Analysis:** Examine data from live events such as sports games or concerts, providing real-time stats, updates, or insights to viewers and commentators.


## Prerequisites

To run the pipeline, you need the following:

- Python 3.7 or above
- Apache Beam (Python SDK)
- Apache Beam dependencies (e.g., `apache-beam[gcp]` for running on Google Cloud Dataflow)
- Apache Beam runners compatible with your execution environment (e.g., Apache Flink, Apache Spark, or Google Cloud Dataflow)

## Getting Started

1. Clone this repository:

   ```bash
   git clone <repository_url>

2. Initializing a virtual environment:

    ```bash
    python -m venv .venv

3. Activating the virtual environment:

* For Windows
    ```bash
    cd .venv/scripts
    .\activate

* For MacOS
    ```bash
    source .venv/bin/activate

4. Activating the virtual environment:

    ```bash
    cd .venv/scripts
    .\activate

5. Installing requirements:

    ```bash
    pip install -r requirements.txt

6. Running the main pipeline:

    ```bash
    python main.py

7. Running the unit tests:

    ```bash
    python -m unittest discover -s . -p "*tests.py"

8. Running the entire project at once:
* For Windows:
    ```bash
    .\run.bat

* For MacOS:
    ```bash
    chmod +x run.sh
    ./run.sh