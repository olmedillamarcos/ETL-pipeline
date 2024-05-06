# Data pipeline with Docker Compose, Airflow, Databricks, Azure Data Lake Gen2 & Azure SQL

## Overview
---
* A ```docker-compose.yml``` file runs Airflow's webserver, scheduler and worker in docker containers.
* Python scripts do API calls to fetch data incrementally from open-meteo.com, a free open-source weather API.
* The data then is stored in a container in Azure Data Lake Gen2
* From there, a Databricks job is run to read the data from the lake, transform it accordingly and store it in a Azure SQL database.

## How the pipeline works
---
* In the Airflow UI create connections for both Azure Blob Storage and Databricks
* Create a new job in databricks to have a job_id to use
* Run ```docker compose up```
  
![dataflow](https://github.com/olmedillamarcos/ETL-pipeline/assets/44475179/62769e6f-5ec7-460a-ad91-f6e688a34516)
