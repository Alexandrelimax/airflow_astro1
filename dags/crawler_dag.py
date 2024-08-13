import requests
from app.database.ConnectionPostgres import ConnectionPostgres
from app.repository.VehicleRepository import VehicleRepository
from app.utils.format_response import format_value

from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

def fetch_vehicle_data():
    url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'
    payload = {
        "codigoTabelaReferencia": 312,
        "codigoTipoVeiculo": 1,
        "anoModelo": 2008,
        "codigoTipoCombustivel": 1,
        "tipoVeiculo": "carro",
        "modeloCodigoExterno": "024112-1",
        "tipoConsulta": "codigo"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def process_and_save_data(**context):
    data = context['task_instance'].xcom_pull(task_ids='fetch_vehicle_data')
    
    vehicle_data = {
        "valor": format_value(data['Valor']),
        "marca": data["Marca"],
        "modelo": data["Modelo"],
        "ano_modelo": str(data["AnoModelo"]),
        "combustivel": data["Combustivel"],
        "codigo_fipe": data["CodigoFipe"],
        "mes_referencia": data["MesReferencia"].strip(),
        "autenticacao": data["Autenticacao"],
        "tipo_veiculo": str(data["TipoVeiculo"]),
        "sigla_combustivel": data["SiglaCombustivel"],
        "data_consulta": data["DataConsulta"]
    }
    
    connection = ConnectionPostgres()
    repository = VehicleRepository(connection)
    repository.insert(vehicle_data)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'vehicle_data_dag',
    default_args=default_args,
    description='DAG: Persiste requisições feitas da FIPE para o banco de dados',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

fetch_task = PythonOperator(
    task_id='fetch_vehicle_data',
    python_callable=fetch_vehicle_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_and_save_data',
    python_callable=process_and_save_data,
    provide_context=True,
    dag=dag,
)

fetch_task >> process_task
