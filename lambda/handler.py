import json
import requests
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'emaseku-s3-covid-bucket'  # Change if needed

def lambda_handler(event, context):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,litecoin,ripple',
        'vs_currencies': 'usd'
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
    filename = f"crypto-prices/{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(data),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': f'Successfully saved {filename}'
    }
