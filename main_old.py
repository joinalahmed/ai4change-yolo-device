import time
import json
from communication import Communication

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

topicIn = "products"

communication = Communication()

# Connect and subscribe to AWS IoT
communication.connect()
communication.subscribe("#", customCallback)
time.sleep(2)

# Publish to the topic in a loop forever
loopCount = 0
while True:
    message = {}
    message['product'] = "tomato"
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    communication.publish(topicIn, messageJson)
    print('Published topic %s: %s\n' % (topicIn, messageJson))
    loopCount += 1
    time.sleep(10)
