import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import storage

# GCP認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

# GCSクライアントAPIの利用宣言
client = storage.Client()

# GCSバケット取得
bucket = client.get_bucket(OperationObject.bucket_name)

# CSVファイルアップロード
blob = bucket.blob(os.path.basename(OperationObject.source_file_name))
blob.upload_from_filename(OperationObject.source_file_name)

print('File {} uploaded to {}.'.format(
    OperationObject.source_file_name,
    bucket))
