#Importing the DAG from the AIRFLOW
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

#defining the common parameters
default_args = {
    'owner': 'harshitha',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_cron_expression_v3',
    default_args=default_args,
    description='This is our first dag we are writing',
    start_date= datetime(2022, 11, 1),
    schedule_interval='0 3 * * 2'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression"
    )

    task1