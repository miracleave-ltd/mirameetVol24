# GCP各種サービスの設定
この手順では次の手順を進めていきます。  


## GCSバケット作成
グローバルに一意になるように各自設定を行います。  
![](img/GCSバケット作成1.png)
![](img/GCSバケット作成2.png)
↓作成完了  
![](img/GCSバケット作成3.png)

## GCS内権限設定
GCSの権限を「ストレージ管理者」に設定します。  
![](img/GCS内権限設定.png)

## サービスアカウントの作成
![](img/サービスアカウントの作成1.png)
![](img/サービスアカウントの作成2.png)
![](img/サービスアカウントの作成3.png)
↓作成完了  
![](img/サービスアカウントの作成4.png)

## 秘密鍵ファイルの取得・配置
![](img/秘密鍵の作成1.png)
![](img/秘密鍵の作成2.png)
※json形式のキーをダウンロード  
![](img/秘密鍵の作成3.png)
ダウンロードした秘密鍵ファイルを、配置する。  
・配置先  
```
mirameet_vol24\credential
```
・ファイル名  
```
key.json
```
## BigQueryAPIの有効化
![](img/BigQueryAPIの有効化1.png)
![](img/BigQueryAPIの有効化2.png)
↓完了  
![](img/BigQueryAPIの有効化3.png)

## データセットの作成
![](img/データセットの作成1.png)
↓完了  
![](img/データセットの作成2.png)

## テーブルの作成
![](img/テーブルの作成1.png)
\mirameet_vol24\sql\mira_vol24.sql  
をご自身の作成したデータセットIDに置換してクエリ実行  
（例）  
```
CREATE TABLE mira_vol24.mira_example　～～～
↓
CREATE TABLE sechico_0905.mira_example　～～～
```
↓実行完了  
![](img/テーブルの作成2.png)

## OperationObject.pyの編集
### url_gs_example_csv  
![](img/url_gs_example_csv.png)
「gsutil URI」をコピーして置換  
（例）  
```
url_gs_example_csv="gs://mira-example/gcs-example.csv"
↓
url_gs_example_csv="gs://sechico-mirameet_vol24/gcs-example.csv"
```
### bucket_name
![](img/bucket_name.png)
「名前」をコピーして置換  
（例）  
```
bucket_name = "mira-example"
↓
bucket_name = "sechico-mirameet_vol24"
```
### project_id
![](img/project_id.png)
```
「プロジェクトID」をコピーして置換  
（例）  
project_id = "erudite-pride-323410"
↓
project_id = "sylvan-surf-322711"
```
### dataset_id
![](img/dataset_id.png)
「データセットID」をコピーして置換  
（例）  
```
dataset_id = "mira_vol24"
↓
dataset_id = "sechico_0905"
```
### table_id　←テーブル作成時のクエリから変えている場合  
![](img/table_id.png)
「テーブルID」をコピーして置換  
（例）  
```
table_id = "mira-example"
↓
table_id = "mira-example"　←テーブル作成時のクエリ
```
