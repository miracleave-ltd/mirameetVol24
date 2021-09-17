import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# テーブルIDの取得
client = bigquery.Client(OperationObject.project_id)
table_id = client.dataset(OperationObject.dataset_id).table(OperationObject.table_id)

# テーブル設定宣言
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "NUMERIC"),
        bigquery.SchemaField("mira_code", "STRING"),
        bigquery.SchemaField("mira_text", "STRING"),
        bigquery.SchemaField("work_date", "STRING")
    ],
    skip_leading_rows=0,
    # CSV形式
    source_format=bigquery.SourceFormat.CSV,
)
# 実行前にテーブルをトランケート
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

# GCSバケットをロードし、テーブルに登録
load_job = client.load_table_from_uri(
    OperationObject.url_gs_example_csv, table_id, job_config=job_config
)  # GCSクライアントAPIへリクエスト

load_job.result()  # リザルト結果を取得

destination_table = client.get_table(table_id)  # GCSクライアントAPIへリクエスト
print("Loaded {} rows.".format(destination_table.num_rows))
