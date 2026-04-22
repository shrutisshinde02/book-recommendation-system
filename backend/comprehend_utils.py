import boto3
from backend.config import AWS_REGION

comprehend = boto3.client("comprehend", region_name=AWS_REGION)

def extract_keywords(text):
    response = comprehend.detect_key_phrases(
        Text=text,
        LanguageCode='en'
    )

    keywords = [phrase['Text'].lower() for phrase in response['KeyPhrases']]
    return keywords