import boto3
from botocore.exceptions import ClientError
from app import config
import io


class Storage:
    project_name = config.AWS_PROJECT_NAME
    bucket_name = config.AWS_BUCKET_NAME
    session = boto3.session.Session()
    contentType_map = {
        'png':'image/png',
        'jpeg':'image/jpeg',
        'jpg':'image/jpg',
        'gif':'image/gif',
        'mp4':'video/mp4',
        'webm':'video/webm',
        'pdf':'application/pdf'
    }

    client = session.client ('s3',
                            region_name = config.AWS_REGION,
                            endpoint_url = config.AWS_BUCKET_ENDPOINT,
                            aws_access_key_id=config.AWS_ACCESS_KEY,
                            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)

    def put_url(self, file_key):
        return self.client.generate_presigned_url(ClientMethod='put_object',
                                                Params={'Bucket': self.bucket_name,
                                                        'Key': f'{self.project_name}/{file_key}'},
                                                ExpiresIn=300) 

    def upload_file(self, file_key, file, file_format) -> tuple:
        try:
            contentType = self.contentType_map[file_format]
        except KeyError:
            return False, 'Formato de arquivo enviado inválido.'
        try:
            response = self.client.upload_fileobj(file, self.bucket_name, 
                                                    f'{self.project_name}/{file_key}',
                                                    ExtraArgs={'ContentType':contentType, 'ACL':'public-read'})
        except ClientError as e:
            return False, e
        return True, ''
    
    def get_download_url(self, file_key) -> tuple:
        return self.client.generate_presigned_url(ClientMethod='get_object',
                                                Params={'Bucket':   self.bucket_name,
                                                        'Key': f'{self.project_name}/{file_key}',
                                                        'ResponseContentDisposition': 'attachment'},
                                                ExpiresIn=300)
        
    def get_url(self, file_key):
        return self.client.generate_presigned_url(ClientMethod='get_object',
                                                Params={'Bucket':   self.bucket_name,
                                                        'Key': f'{self.project_name}/{file_key}'},
                                                ExpiresIn=300)
                                        
    def delete_object(self, file_key):
        self.client.delete_object(Bucket= self.bucket_name,
                                  Key=f'{self.project_name}/{file_key}')

    def delete_objects(self, keys) -> None:
        self.client.delete_objects(Bucket= self.bucket_name,
                                   Delete={'Objects': keys,
                                           'Quiet': True})


storage = Storage()