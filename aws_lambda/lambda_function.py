import json

def lambda_handler(event, context):
    mapping = {
        "tomato": "cucumber",
        "cucumber": "tomato",
        "apple_green": "apple_red",
        "apple_red": "grape",
        "banana": "apple_green",
        "coca_cola": "sweets_7_days",
        "egg": "water",
        "grape": "banana"
        "pepper_red": "egg",
        "sweets_7_days": "sweets_snickers",
        "sweets_mms": "coca_cola",
        "sweets_nesquik": "sweets_mms",
        "sweets_snickers": "sweets_nesquik",
        "water": "pepper_red"
    }
    
    if event["product"] in mapping:
        return {
            "recommendation": mapping[event["product"]]
        }
    else:
        return {
            "recommendation": "nothing"
        }