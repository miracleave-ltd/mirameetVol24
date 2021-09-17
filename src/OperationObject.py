# ------------------------------------------------------
# 変数
# ------------------------------------------------------
GOOGLE_APPLICATION_CREDENTIALS='./credential/key.json'

# CSVコピー元
source_file_name = './csv/gcs-example.csv'

# CSV配置先
url_gs_example_csv="gs://mira-example/gcs-example.csv" # 手順1.1
# CSVダウンロード先
out_url_gs_example_csv="gs://mira-example/out-gcs-example.csv" # 手順1.1

# GCSバケット
bucket_name = "mira-example" # 手順1.2

# 操作テーブル
project_id = "erudite-pride-323410" # 手順1.3
dataset_id = "mira_vol24" # 手順1.4
table_id = "mira_example" # 手順1.5
