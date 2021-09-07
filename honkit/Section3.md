# 各処理の実行と処理結果の確認

## カレントディレクトリの移動
```
cd ～～～\mirameet_vol24
```

## GcsUploader01.pyの実行
```
python GcsUploader01.py
```
![](img/01-2.png)  
CSVファイルがGCSにアップロードされていることを確認。
![](img/01.png)  

## GcsToBigQuery02.pyの実行
```
python GcsToBigQuery02.py
```
![](img/02-2.png)  
CSVの中のデータがBigQueryにインサートされていることを確認。
![](img/02.png)  

## UpdateDeleteBigQuery03.pyの実行
```
python UpdateDeleteBigQuery03.py
```
![](img/03-2.png)  
データが更新・削除されていることを確認。
![](img/03.png)  

## ExportBigQuery04.pyの実行
```
python ExportBigQuery04.py
```
![](img/04-2.png)  
BigQueryのデータが「out-gcs-example.csv」ファイルとしてGCSに出力されていることを確認。
![](img/04.png)  