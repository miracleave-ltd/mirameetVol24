import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# テーブルIDの取得
client = bigquery.Client(OperationObject.project_id)
table_id = client.dataset(OperationObject.dataset_id).table(OperationObject.table_id)

#　データ取得結果をGSバケットに配置 
extract_job = client.extract_table(
    table_id,
    OperationObject.out_url_gs_example_csv,
)  # クライアントAPIへリクエスト
extract_job.result() # extract_tableが終了するまで待機

print(
    "Exported {}:{}.{} to {}".format(
        OperationObject.project_id,
        OperationObject.dataset_id,
        OperationObject.table_id,
        OperationObject.out_url_gs_example_csv)
)
