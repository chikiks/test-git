from airflow.models.dag import DAG
import datetime
import pendulum

from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    # 분/시/일/월/요일
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 4, 1, tz="Asia/Seoul"),
    # 과거 미수행 일자도 돌릴지 여부
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["keyword_#1", "keyword_#2"],
    params={"example_key": "example_value"},
) as dag:
    
    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    # [END howto_operator_bash]

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2