# from datetime import datetime

# from airflow import DAG
# from airflow.operators.bash import BashOperator


# default_args = {
#     "owner": "chanithi",
# }


# with DAG(
#     dag_id="ecommerce_etl_pipeline",

#     default_args=default_args,

#     start_date=datetime(2026, 1, 1),

#     schedule="@daily",

#     catchup=False,
# ) as dag:

#     run_etl = BashOperator(

#         task_id="run_etl_pipeline",

#         bash_command="""
#         cd ~/batch_pipeline_project &&
#         source airflow_venv/bin/activate &&
#         python scripts/load_data.py
#         """
#     )
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# from datetime import datetime
# import sys
# import os

# # add project root to python path
# sys.path.append(
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__), "..")
#     )
# )

# from scripts.load_data import main


# default_args = {
#     "owner": "chanithi"
# }


# with DAG(
#     dag_id="ecommerce_etl_pipeline",
#     default_args=default_args,
#     start_date=datetime(2024, 1, 1),
#     schedule="@daily",
#     catchup=False
# ) as dag:

#     run_etl = PythonOperator(
#         task_id="run_etl_pipeline",
#         python_callable=main
#     )
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# Import ETL main function
from scripts.load_data import main

# Default DAG arguments
default_args = {
    "owner": "chanithi"
}

# Define DAG
with DAG(
    dag_id="ecommerce_etl_pipeline",
    default_args=default_args,
    description="Batch ETL pipeline for ecommerce data",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "batch-pipeline"]
) as dag:

    # ETL task
    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=main
    )

    run_etl