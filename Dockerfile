FROM apache/airflow:2.8.1
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark && \
    pip install --no-cache-dir apache-airflow-providers-databricks  