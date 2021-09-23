import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCP認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# BigQueryクライアントAPIを利用宣言
client = bigquery.Client(OperationObject.project_id)

# テーブル情報の取得
table_info = client.dataset(OperationObject.dataset_id).table(OperationObject.table_id)

# JOB設定情報の定義を実施
job_config = bigquery.LoadJobConfig(
    # テーブルカラムマッピング情報の設定
    schema=[
        bigquery.SchemaField("id", "NUMERIC"),
        bigquery.SchemaField("mira_code", "STRING"),
        bigquery.SchemaField("mira_text", "STRING"),
        bigquery.SchemaField("work_date", "STRING")
    ],
    # 読み込み開始行の指定（ヘッダ行がないため0を設定）
    skip_leading_rows=0,
    # ソースフォーマットの指定（CSV形式に設定）
    source_format=bigquery.SourceFormat.CSV,
)

# GCSバケットをロードし、テーブルに登録
load_job = client.load_table_from_uri(
    OperationObject.url_gs_example_csv, table_info, job_config=job_config
)  # クライアントAPIへリクエスト

load_job.result()  # load_table_from_uriが終了するまで待機

destination_table = client.get_table(table_info)  # クライアントAPIへリクエスト（テーブル情報を取得）
print("Loaded {} rows.".format(destination_table.num_rows))
