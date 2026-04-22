import json
from recommender import get_recommendations

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_input = body.get("preferences", "")

        recommendations = get_recommendations(user_input)

        return {
            "statusCode": 200,
            "body": json.dumps(recommendations)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }