from storages.backends.s3boto3 import S3Boto3Storages

class StaticStorage(S3Boto3Storages):
    location = "static/"
    file_overwrite = False

class UploadStorage(S3Boto3Storages):
    location = "uploads/"