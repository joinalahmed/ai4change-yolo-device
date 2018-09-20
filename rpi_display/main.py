import json
import os
import cv2
import time
#from communication import Communication

image_base_path = os.path.join(os.getcwd(), "images")
image_extension = "jpg"
json_as_string = """{"output":{"recommendation":"test1"}}"""
raw_json = json.loads(json_as_string)

#mqtt_topic = "advice"

def get_recommendation_from_json (raw_json):
    parsed_json = raw_json['output']['recommendation']
    return parsed_json

def show_image(image_base_path, image_name, image_extension):
    img = cv2.imread(os.path.join(image_base_path, (image_name + "." + image_extension)))
    img_resized = cv2.resize(img, (480, 320))
    cv2.imshow(image_name, img_resized)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()

#def customCallback(client, userdata, message):
#    print("Received a new message: ")
#    print(message.payload)
#    print("from topic: ")
#    print(message.topic)
#    print("--------------\n\n")


#communication = Communication()

#communication.connect()
#communication.subscribe(mqtt_topic, customCallback)
#time.sleep(2)

recommendation = get_recommendation_from_json(raw_json)
show_image(image_base_path, recommendation, image_extension)

