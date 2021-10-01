# おまけ
この手順では、作成したテーブルやバケットの削除をします  

※無料期間が終了しても自動で課金されることはありません  
　GCP内をCleanUpしたい方は以下手順を行ってください  

## バケットの削除  
![](img/bucket_delete.png)  

![](img/bucket_delete2.png)  


## データセットの削除  
![](img/table_delete.png)  

![](img/table_delete2.png)  


## Dockerコンテナの停止  
起動中のコンテナの確認  
```
docker-compose ps
```
コンテナの停止  
```
docker-compose down
```
コンテナが停止されたことの確認  
```
docker-compose ps
```
![](img/docker_down.png)  
