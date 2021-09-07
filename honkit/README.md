# GCP初心者必見！ PythonでBigQueryの操作をしてみよう！<br/>
第24回目の開催となるmirameetの題材はGCP初心者必見★
今回のハンズオンはGoogle Cloud Storageの開発Tipsも取り込んだ内容になっています！

## 事前準備
- Dockerインストール
- GitHubアカウント
- GCPアカウント

## 今回の流れ
CSVファイルをGCS（GoogleCloudStroage）上にアップロード、
CSVファイルのデータをBigQueryに投入、
BigQuery内のデータを確認するバッチを作成し実行します。


## 技術要素
- [GCP](https://console.cloud.google.com/?hl=ja)
- [Docker](https://www.docker.com/)
- [python](https://www.python.jp/)


## 手順
全体手順としては次の流れで進めます。
![](img/45.png)  
- ①事前準備内容の確認
- ②GCP各種サービスの設定
- ③各処理の実行と処理結果の確認

---

Windows/Macの方向けに作成しております。  
コマンドラインツールは、個々の利用しているもので良いのですが、今回の手順は次のものを利用します。  
- Windows：コマンドプロンプト
- Mac：ターミナル
