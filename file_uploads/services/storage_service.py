import boto3
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import io

class StorageService:
    @staticmethod
    def upload_to_s3(file_name, content):
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=content)
        return f"https://{bucket_name}.s3.{settings.AWS_REGION}.amazonaws.com/{file_name}"

    @staticmethod
    def save_to_file_system(file_name, content):
        file_like_object = io.BytesIO(content)
        file_path = default_storage.save(file_name, ContentFile(file_like_object.read()))
        return default_storage.url(file_path)
    
    @staticmethod
    def save_file(file_name, content):
        if settings.USE_S3:
            return StorageService.upload_to_s3(file_name, content)
        return StorageService.save_to_file_system(file_name, content)
