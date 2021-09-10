import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import storage

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# GCSクライアント変数宣言
client = storage.Client()

# GSバケット取得
bucket = client.get_bucket(OperationObject.bucket_name)

# CSVファイルアップロード
blob = bucket.blob(os.path.basename(OperationObject.source_file_name))
blob.upload_from_filename(OperationObject.source_file_name)

print('File {} uploaded to {}.'.format(
    OperationObject.source_file_name,
    bucket))
