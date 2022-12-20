from airflow.decorators import dag, task
from datetime import datetime,timedelta

default_args = {
    'owner': 'Harshitha shekar',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}

@dag(
    dag_id='dag_with_task_flow_api_v2',
    start_date=datetime(2022, 12,11),
    schedule_interval='@daily'
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Harshitha',
            'last_name': 'Shekar'
        }

    @task()
    def get_age():
        return 23

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! Mu name is {first_name} {last_name} and I am {age} years old")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'],age=age)

greet_dag = hello_world_etl()
