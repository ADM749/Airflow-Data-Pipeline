from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta

# Hide everything inside a function so the scanner ignores it
def read_and_send_email():
    # 1. Read the file ONLY when the task actually runs
    with open('/data/output.txt', 'r') as f:
        body = f.read()
    
    # 2. Send the email directly from this Python function
    send_email(
        to=['debem34769@flosek.com', 'am7602091@gmail.com'],
        subject='test Airflow Mail',
        html_content=body
    )

with DAG(dag_id='Dag4',
         start_date=datetime(2026, 3, 14),
         schedule_interval=timedelta(minutes=5),
         catchup=False
         ) as dag:

    # 3. Trigger the function using a standard PythonOperator
    task1 = PythonOperator(
        task_id='send_email_task',
        python_callable=read_and_send_email
    )