from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'harshitha',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name',key='last_name')
    age = ti.xcom_pull(task_ids='get_age',key='age')

    print(f"Hello world! my name is {first_name + last_name}, and I am {age} years old")


def get_name(ti):
    ti.xcom_push(key='first_name',value='Harshitha')
    ti.xcom_push(key='last_name',value='Shekar')


def get_age(ti):
    ti.xcom_push(key='age',value=20)

with DAG(
    dag_id='greet_user',
    default_args=default_args,
    description='This is our first dag using python operator',
    start_date= datetime(2022, 12, 11, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )    
    
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    task2>>task1
    task3>>task1