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

#creating an instance of DAG using the "with" statement.
# In this case all the code will be under the scope of "dag" instance. 
with DAG(
    dag_id='our_first_dag_v2',
    default_args=default_args,
    description='This is our first dag we are writing',
    start_date= datetime(2022, 12, 12, 6),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo hey I am the second task and will be running after the task 1"
    )

    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo hey I am the third task and will be running after task 1 and at the same time of task 2"
    )
    #update the dependencies
    #task 2 as the downstream of task1 or we can set as task1 as the upstream of task
    #ie., task2.set_upstream(task1)
    # task dependency method1
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # task dependency method 2 similar to above command but using bit operator
    # task1 >> task2
    # task1 >> task3

    # task dependency method 3
    # task1 >> [task2, task3]