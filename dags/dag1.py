from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta



with DAG (dag_id = 'Dag1',
        start_date = datetime(2025,3,14),
        schedule_interval = timedelta(minutes=5),
        catchup = False
        ) as dag:
   
    task1 = BashOperator(
        task_id = 'hello_world',
        bash_command = 'echo "Adam Mohamed"'
    )

task1
