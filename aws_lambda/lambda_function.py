import json

def lambda_handler(event, context):
    mapping = {
        "tomato": "cucumber",
        "cucumber": "tomato"
    }

    return {
        "recommendation": mapping[event["product"]]
    }
