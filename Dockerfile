FROM apache/airflow:2.5.0

COPY ./dags $AIRFLOW_HOME/dags