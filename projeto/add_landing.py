import boto3
from faker import Faker
import io



if __name__ == '__main__':
    # Configurar Faker
    fake = Faker()

    s3 = boto3.client(
        's3',
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name='us-east-1',
        endpoint_url='http://localhost:4566'
    )

    #nome bucket
    bucket_name = 'landing-zone'

    #gerador de arquivo
    for _ in range(50):
        file_name = f"{fake.uuid4()}.txt"
        file_content = fake.text()

        #objeto arquivo memoria
        file_obj = io.BytesIO(file_content.encode())
        #upload arquivos s3
        s3.upload_fileobj(file_obj, bucket_name, file_name)
        print(f"Arquivo enviado: {file_name}")

#listar arquivos bucket
for obj in s3.list_objects(Bucket=bucket_name)['Contents']:        
    print(obj['Key'])

