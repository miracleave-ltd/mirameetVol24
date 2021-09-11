# 各処理の実行と処理結果の確認  
この手順では、コーディングしたソースを動かし、BigQueryのデータを操作していきます。
![](img/draw_flow_3.png)  


## カレントディレクトリの移動  
Zipファイルを解凍したディレクトリまで移動  
```
cd ～～～mirameetVol24-main
```

## Dockerでコンテナを起動  
```
docker-compose up -d --build
```
![](img/docker-build.png)  

## カレントディレクトリの移動  
srcディレクトリまで移動  
```
cd ～～～mirameetVol24-main\src
```

## GcsUploader01.pyの実行  
★★★画像差し込み★★★  
CSVデータファイルをGCSバケット上にアップロードする  
```
python GcsUploader01.py
```
▼中身
```
import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import storage

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# GCSクライアント変数宣言
client = storage.Client()

# GCSバケット取得
bucket = client.get_bucket(OperationObject.bucket_name)

# CSVファイルアップロード
blob = bucket.blob(os.path.basename(OperationObject.source_file_name))
blob.upload_from_filename(OperationObject.source_file_name)

print('File {} uploaded to {}.'.format(
    OperationObject.source_file_name,
    bucket))
```
↓正常終了  
![](img/01py01.png)  
mirameetVol24-main\src\csvの中の「gcs-example.csv」が、GCSにアップロードされていることを確認  
![](img/01py02.png)  

## GcsToBigQuery02.pyの実行  
★★★画像差し込み★★★  
GCSにアップロードしたCSVデータをBigQueryにインサートする  
```
python GcsToBigQuery02.py
```
▼中身
```
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
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# 実行前にテーブルをトランケート
job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

# GSバケットをロードし、テーブルに登録
load_job = client.load_table_from_uri(
    OperationObject.url_gs_example_csv, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))

```
↓正常終了  
![](img/02py01.png)  
「gcs-example.csv」の中のデータがBigQueryにインサートされていることを確認  
プレビュータグでデータの中身を確認  
![](img/02py03.png)  

## UpdateDeleteBigQuery03.pyの実行  
★★★画像差し込み★★★  
BigQueryのデータを更新・削除する  
```
python UpdateDeleteBigQuery03.py
```
▼中身
```
import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

client = bigquery.Client()
# 更新SQL生成
updateQuery = "UPDATE `{0}.{1}.{2}` SET mira_text = '更新' WHERE id = 2".\
    format(OperationObject.project_id, OperationObject.dataset_id, OperationObject.table_id)
# SQL実行
updateRows = client.query(updateQuery).result()
print("Updated ID=2.")

# 削除SQL生成
deleteQuery = "DELETE `{0}.{1}.{2}` WHERE id = 3".\
    format(OperationObject.project_id, OperationObject.dataset_id, OperationObject.table_id)
# SQL実行
deleteRows = client.query(deleteQuery).result()

print("deleted ID=3.")
```
↓正常終了  
![](img/03py01.png)  
ID＝2のデータが更新、ID＝3のデータが削除されていることを確認  
![](img/03py02.png)  

## ExportBigQuery04.pyの実行  
★★★画像差し込み★★★  
BigQueryのデータをCSVデータファイルとしてGCSバケットにエクスポートする  
```
python ExportBigQuery04.py
```
▼中身
```
import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# テーブルIDの取得
client = bigquery.Client(OperationObject.project_id)
table_id = client.dataset(OperationObject.dataset_id).table(OperationObject.table_id)

extract_job = client.extract_table(
    table_id,
    OperationObject.out_url_gs_example_csv,
)  # API request
extract_job.result()  # Waits for job to complete.

print(
    "Exported {}:{}.{} to {}".format(
        OperationObject.project_id,
        OperationObject.dataset_id,
        OperationObject.table_id,
        OperationObject.out_url_gs_example_csv)
)
```
↓正常終了  
![](img/04py01.png)  
BigQueryのデータが「out-gcs-example.csv」ファイルとしてGCSに出力されていることを確認  
![](img/04py02.png)  
ダウンロードボタンでファイルをローカルにダウンロード  
![](img/04py03.png)  
ダウンロードしたCSVファイルの中身で更新後の状態を確認  
![](img/04py04.png)  

