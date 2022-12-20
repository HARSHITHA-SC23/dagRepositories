from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'harshitha',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchup_and_backfill_v1',
    default_args=default_args,
    description='This is our first dag we are writing',
    start_date= datetime(2022, 12, 11),
    schedule_interval='@daily',
    catchup=True  # by default it is set to True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo hello world, this is the first task!"
    )
