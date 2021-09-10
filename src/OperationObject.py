# ------------------------------------------------------
# 変数
# ------------------------------------------------------
GOOGLE_APPLICATION_CREDENTIALS='./credential/key.json'

# CSVコピー元
source_file_name = './csv/gcs-example.csv'

# GS バケット
bucket_name = "mira-example"

url_gs_example_csv="gs://mira-example/gcs-example.csv"
out_url_gs_example_csv="gs://mira-example/out-gcs-example.csv"

# 操作テーブル
project_id = "erudite-pride-323410" # 要変更
dataset_id = "mira_vol24"
table_id = "mira_example"
