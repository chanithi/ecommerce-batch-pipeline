# # from datetime import datetime

# # from airflow import DAG
# # from airflow.operators.bash import BashOperator


# # default_args = {
# #     "owner": "chanithi",
# # }


# # with DAG(
# #     dag_id="ecommerce_etl_pipeline",

# #     default_args=default_args,

# #     start_date=datetime(2026, 1, 1),

# #     schedule="@daily",

# #     catchup=False,
# # ) as dag:

# #     run_etl = BashOperator(

# #         task_id="run_etl_pipeline",

# #         bash_command="""
# #         cd ~/batch_pipeline_project &&
# #         source airflow_venv/bin/activate &&
# #         python scripts/load_data.py
# #         """
# #     )
# # from airflow import DAG
# # from airflow.operators.python import PythonOperator

# # from datetime import datetime
# # import sys
# # import os

# # # add project root to python path
# # sys.path.append(
# #     os.path.abspath(
# #         os.path.join(os.path.dirname(__file__), "..")
# #     )
# # )

# # from scripts.load_data import main


# # default_args = {
# #     "owner": "chanithi"
# # }


# # with DAG(
# #     dag_id="ecommerce_etl_pipeline",
# #     default_args=default_args,
# #     start_date=datetime(2024, 1, 1),
# #     schedule="@daily",
# #     catchup=False
# # ) as dag:

# #     run_etl = PythonOperator(
# #         task_id="run_etl_pipeline",
# #         python_callable=main
# #     )
# from airflow import DAG
# from airflow.operators.python import PythonOperator

# from datetime import datetime
# import sys
# import os

# # Add project root to Python path
# sys.path.append(
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__), "..")
#     )
# )

# # Import pipeline stages
# from scripts.extract import extract_data
# from scripts.clean import clean_data
# from scripts.transform import transform_data
# from scripts.load import load_data
# from scripts.quality_check import run_quality_checks

# # Import ETL main function
# from scripts.load_data import main

# # Default DAG arguments
# default_args = {
#     "owner": "chanithi"
# }

# # Define DAG
# with DAG(
#     dag_id="ecommerce_etl_pipeline",
#     default_args=default_args,
#     description="Batch ETL pipeline for ecommerce data",
#     start_date=datetime(2024, 1, 1),
#     schedule="@daily",
#     catchup=False,
#     tags=["etl", "batch-pipeline"]
# ) as dag:

#     # ETL task
#     run_etl = PythonOperator(
#         task_id="run_etl_pipeline",
#         python_callable=main
#     )

#     run_etl

from airflow import DAG
from airflow.operators.python import PythonOperator


from datetime import datetime, timedelta
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# Import pipeline stages
from scripts.extract import extract_data
from scripts.clean import clean_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.quality_check import run_quality_checks
from scripts.sql_transform import transform_sales_table

# Default arguments
default_args = {
    "owner": "chanithi",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
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

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id="load_to_database",
        python_callable=load_data
    )

    sql_transform_task = PythonOperator(
    task_id="transform_sales_table",
    python_callable=transform_sales_table
    )

    quality_check_task = PythonOperator(
        task_id="run_quality_checks",
        python_callable=run_quality_checks
    )

    

    # Task dependencies
    (
        extract_task
        >> clean_task
        >> transform_task
        >> load_task
        >> sql_transform_task
        >> quality_check_task
    )