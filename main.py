# Script used to show recommended image based on call recieved from MQTT
# The workflow is following:
# 1. Using RaspberryPi, Intel Movidius and a camera, the item in the basket is recognized
# 2. The name of recognized item is sent to AWS via MQTT (using "products" topic)
# 3. On AWS the recommendation is generated (using AWS Lambda)
# 4. The recommendation is sent back to RaspberryPi via MQTT (using "advice" topic)
# 5. Based on the reciveded recommendation, the image is displayed on the screen.

# This script is taking care of points #4 and #5.

# Imports
import json
import os
import cv2
import time
from communication import Communication

# Set parameters
image_base_path = os.path.join(os.getcwd(), "images")
image_extension = "jpg"
mqtt_topic = "advice"

# The recommendation recieved via MQTT is stored in json format.
# Function get_recommendation_from_json is parsing this json to extract information required to show correct image
def get_recommendation_from_json (raw_json):
    parsed_json = raw_json['output']['recommendation']
    return parsed_json

# Function show_image is used to open correct image (based on recommendation recieved via MQTT)
# and show it on the screen plugged to RaspberryPi
def show_image(image_base_path, image_name, image_extension):
    img = cv2.imread(os.path.join(image_base_path, (image_name + "." + image_extension)))
    img_resized = cv2.resize(img, (480, 320))
    cv2.imshow(image_name, img_resized)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()

# Put everything together into the workflow
def customCallback(client, userdata, message):
	raw_json = json.loads(message.payload)
	recommendation = get_recommendation_from_json(raw_json)
	show_image(image_base_path, recommendation, image_extension)

# initialize Communication with AWS and subscribe "advice" topic
communication = Communication()
communication.connect()
communication.subscribe(mqtt_topic, customCallback)

while True:
	time.sleep(10)


