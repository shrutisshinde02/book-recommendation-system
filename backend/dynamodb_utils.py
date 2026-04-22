import boto3
from backend.config import AWS_REGION, TABLE_NAME

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

def get_all_books():
    response = table.scan()
    return response.get('Items', [])

print("Using table:", TABLE_NAME)    