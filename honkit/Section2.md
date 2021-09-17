# GCP各種サービスの設定  
この手順では、GCPサービスの設定を進めていきます。  
![](img/draw_flow_1.png)  


## GCSバケット作成  
左上のナビゲーションメニューから、CloudStorageを選択  
![](img/GCS01.png)
「バケットを作成」をクリック
![](img/GCS02.png)
グローバルに一意になるように各自設定を行います。  
![](img/GCS03.png)
↓作成完了  
![](img/GCS04.png)

## サービスアカウントの作成  
左上のナビゲーションメニューから、IAMと管理＞サービスアカウントを選択  
![](img/IAM01.png)
任意のサービスアカウント名を入力  
![](img/IAM02.png)
![](img/IAM03.png)
↓作成完了  
![](img/IAM04.png)

## 秘密鍵ファイルの作成・ダウンロード  
作成したサービスアカウントを選択  
![](img/IAM04.png)
「キー」タブ＞「新しい鍵を作成」を選択  
![](img/IAM05.png)
json形式のキーをダウンロード  
![](img/IAM06.png)
↓ダウンロード完了  
![](img/IAM07.png)

## CloudStorageAPIが有効化されていることを確認  
画面上部の検索窓に「Cloud Storage」と入力し、検索結果から「Cloud Storage API」を選択  
![](img/GCS-API01.png)
※「APIが有効です」となっていることを確認  
![](img/GCS-API02.png)

## BigQueryAPIが有効化されていることを確認  
画面上部の検索窓に「BigQuery API」と入力し、検索結果から「BigQuery API」を選択  
![](img/BQ-API01.png)
※「APIが有効です」となっていることを確認  
![](img/BQ-API02.png)

## データセットの作成  
左上のナビゲーションメニューから、BigQueryを選択  
![](img/BQ01.png)
エクスプローラーの中の「▶プロジェクト名」から「データセットを作成」を選択  
![](img/BQ02.png)
画面右側に「データセットを作成する」が出てくるので、「データセットID」を入力  
※今回は「mira_vol24」を指定  
![](img/BQ03.png)
↓完了  
「▶プロジェクト名」の下に「▶mira_vol24」が作成される  
![](img/BQ04.png)

## テーブルの作成  
作成したデータセット「mira_vol24」に対して、クエリを実行し、テーブルを作成  
※今回は「mira_example」を指定 
![](img/BQ04.png)
```
CREATE TABLE mira_vol24.mira_example
(
	id NUMERIC,
	mira_code STRING,
	mira_text STRING,
	work_date STRING
)
```
※データセットIDを「mira_vol24」から変更した場合は、  
　ご自身が指定したデータセットIDに置換して実行する必要があります  
※先ほどDLしたソースファイルの\sql\mira_vol24.sql  の中にも同じSQLがあります  
↓実行完了  
![](img/BQ05.png)
先ほど実行したクエリ通りのフィールドが表示されていることを確認  
![](img/BQ06.png)

このクエリは、  
```
データセットID＝mira_vol24
テーブルID＝mira_example
```
を指定しています  
