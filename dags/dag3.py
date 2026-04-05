from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta



with DAG (dag_id = 'Dag3',
        start_date = datetime(2026,3,14),
        schedule_interval = timedelta(minutes=5),
        catchup = False
        ) as dag:
   
    task1 = BashOperator(
        task_id = 'hello_wExtract',
        bash_command = 'python /data/app.py'
    )

task1
