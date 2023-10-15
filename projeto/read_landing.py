import boto3
import pandas as pd
from io import StringIO

if __name__ == "__main__":
    #configuracao client boto3
    s3 = boto3.client('s3',
                      endpoint_url='http://localhost:4566',
                      aws_access_key_id='test',
                      aws_secret_access_key='test',
                      region_name='us-east-1')
    
    #nome bucket
    bucket_name = 'landing-zone'

    #obter lista de todos os objetos
    objects = s3.list_objects(Bucket=bucket_name)

    #inicializar dataframe vazio
    all_data = pd.DataFrame()   

    #loop para iterar sobre todos os objetos
    for obj in objects.get('Contents',[]):
        #Verificar se o objeto é um arquivo txt
        if obj['Key'].endswith('.txt'):
            #obter objeto
            obj = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
            #ler arquivo txt
            data = obj['Body'].read().decode('utf-8')
            #usar pandas para ler os dados TXT
            df = pd.read_csv(StringIO(data), sep='\t', header=None)
            #concatenar os dados com o dataframe existente
            all_data = pd.concat([all_data, df])    

    #resetar o indice do dataframe concatenado
    all_data.reset_index(drop=True, inplace=True)
    #exibir o resultado como dicionario
    print(all_data.to_dict())        
    #print(all_data.head())  
