from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta

# 1. Hide the file reading and email logic inside this function
def read_and_send_email():
    # The file is only opened when task3 actually executes
    with open('/data/output.txt', 'r') as f:
        body = f.read()
    
    # Send the email directly from Python
    send_email(
        to=['debem34769@flosek.com', 'am7602091@gmail.com'],
        subject='Airflow Mail',
        html_content=body
    )

def fun1():
    for i in range(10):
        print(i)

with DAG(dag_id='Dag5',
         start_date=datetime(2026, 3, 14),
         schedule_interval=timedelta(minutes=5),
         catchup=False
         ) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "welcome mr Adam Mohamed "'
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=fun1
    )

    # 2. Replaced EmailOperator with PythonOperator
    task3 = PythonOperator(
        task_id='task3',
        python_callable=read_and_send_email
    )

    task4 = BashOperator(
        task_id='task4',
        bash_command='python /data/app2.py'
    )

# 3. Dependencies remain exactly the same
task1 >> task2 >> task4 >> task3