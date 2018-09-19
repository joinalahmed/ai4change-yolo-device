import json
import os
import cv2
import time
from communication import Communication

image_base_path = os.path.join(os.getcwd(), "images")
image_extension = "jpg"

mqtt_topic = "advice"

def get_recommendation_from_json (raw_json):
    parsed_json = raw_json['output']['recommendation']
    return parsed_json


def show_image(image_base_path, image_name, image_extension):
    img = cv2.imread(os.path.join(image_base_path, (image_name + "." + image_extension)))
    cv2.imshow(image_name, img)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()

def customCallback(client, userdata, message):
	raw_json = json.loads(message.payload)
	recommendation = get_recommendation_from_json(raw_json)
	show_image(image_base_path, recommendation, image_extension)


communication = Communication()

communication.connect()
communication.subscribe(mqtt_topic, customCallback)
while True:
	time.sleep(10)


