# ------------------------------------------------------
# 変数
# ------------------------------------------------------
GOOGLE_APPLICATION_CREDENTIALS='./credential/key.json'

# CSVコピー元
source_file_name = './csv/gcs-example.csv'

# GS バケット（作成したグローバルユニークなGSバケットに変更してください）
bucket_name = "mira-example"

# CSV配置先（作成したグローバルユニークなGSバケットに変更してください）
url_gs_example_csv="gs://mira-example/gcs-example.csv"
# CSVダウンロード先（作成したグローバルユニークなGSバケットに変更してください）
out_url_gs_example_csv="gs://mira-example/out-gcs-example.csv"

# 操作テーブル
project_id = "erudite-pride-323410" # （使用すｒプロジェクトＩＤに変更してください）
dataset_id = "mira_vol24"
table_id = "mira_example"
