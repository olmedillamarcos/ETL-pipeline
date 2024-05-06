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

  
![dataflow(https://private-user-images.githubusercontent.com/44475179/328203559-62769e6f-5ec7-460a-ad91-f6e688a34516.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTUwMDQ2MzcsIm5iZiI6MTcxNTAwNDMzNywicGF0aCI6Ii80NDQ3NTE3OS8zMjgyMDM1NTktNjI3NjllNmYtNWVjNy00NjBhLWFkOTEtZjZlNjg4YTM0NTE2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTA2VDE0MDUzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg2ZDc0ZDRhZmRlMThlMjczZGExOGI1NzQ5ODBjMDA1YmQ5ODlhNzYxZGUwZDIyZGZhMjdjYzUyZTc1Yjg3MTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.UR3gEe9BpK2LypszlH-p4tdwcGTLktA5jYFxGYdjjH4)](https://github.com/olmedillamarcos/ETL-pipeline/assets/44475179/62769e6f-5ec7-460a-ad91-f6e688a34516)
