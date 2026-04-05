from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta


def fun1():
  print("Welcome to Airflow")

def fun2():
  names = ['Gamal', 'Menna', 'Ahmed', 'Omar', 'Hossam']
  for name in names: 
    print(name)


with DAG (dag_id = 'Dag2',
        start_date = datetime(2026,3,14),
        schedule_interval = timedelta(minutes=10),
        catchup = False
        ) as dag:
   
   task1 = PythonOperator(
       task_id = "task1",
       python_callable = fun1
   )
   task2 = PythonOperator(
       task_id = "task2",
       python_callable = fun2
   )


task1  >> task2