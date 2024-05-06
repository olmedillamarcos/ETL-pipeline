# Data pipeline with Docker Compose, Airflow, Databricks, Azure Data Lake Gen2 & Azure SQL

## Overview
---
* A ```docker-compose.yml``` file runs Airflow's webserver, scheduler and worker in docker containers.
* Python scripts do API calls to fetch data incrementally from open-meteo.com, a free open-source weather API.
* The data then is stored in a container in Azure Data Lake Gen2
* From there, a Databricks job is run to read the data from the lake, transform it accordingly and store it in a Azure SQL database.

## How the pipeline works
---
* Run $docker compose up$
* 
