
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
import airflow.utils.dates

import logging
from pathlib import Path
import requests
import json
from datetime import datetime,timedelta

default_args = {
  'owner': 'airflow'
}

def _fetch_events(ds,**context):

    execution_date = datetime.strptime(ds, '%Y-%m-%d')

    end_date = execution_date - timedelta(days=0)
    start_date = execution_date - timedelta(days=1)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    print(start_date_str,end_date_str)

    response = requests.get("https://archive-api.open-meteo.com/v1/era5?latitude=52.52&"\
    "longitude=13.41&"\
    f"start_date={start_date_str}&"\
    f"end_date={end_date_str}&"\
    "hourly=temperature_2m")

    data = response.json()

    Path("/data/events").mkdir(exist_ok=True,parents=True)

    with open(f'/data/events/{ds}.json', 'w') as f:
        json.dump(data,f)


def _fetch_saved(wasb_conn_id, container, **context):

    ds = context['ds']

    hook=WasbHook(wasb_conn_id)
    logging.info("Exporting JSON to Azure Blob")
    hook.load_file(
        file_path=f'/data/events/{ds}.json', 
        container_name=container,
        blob_name=f"{ds}.json"
    )

dag = DAG(
    dag_id="request_pyhton",
    description="Fetch data using PythonOperator",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval='@daily',
    catchup=True,
    default_args=default_args
)

fetch_events = PythonOperator(
    provide_context=True,
    task_id="fetch_events",
    python_callable=_fetch_events,
    dag = dag,
)

fetch_saved = PythonOperator(
    provide_context=True,
    task_id="fetch_save",
    python_callable=_fetch_saved,
    op_kwargs={
        "wasb_conn_id":"AIRFLOW_CONN_AZURE_DATA_LAKE_GEN2",
        "container":"json"
    },
    dag=dag,
)

data_transformation = DatabricksRunNowOperator(
    dag = dag,
    notebook_params ={"filename":"{{ ds }}"},
    task_id='data_transformation',
    databricks_conn_id = 'databricks_default',
    job_id = 256618961531132
)

fetch_events >> fetch_saved >> data_transformation
