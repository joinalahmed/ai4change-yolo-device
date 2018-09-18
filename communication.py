from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import configparser
import uuid

class Communication:
    def __init__(self):
        Config = configparser.ConfigParser()
        Config.read("communication.ini")

        host = Config.get("IoT","host")
        rootCAPath = Config.get("IoT","rootCAPath")
        certificatePath = Config.get("IoT","certificatePath")
        privateKeyPath = Config.get("IoT","privateKeyPath")
        port = int(Config.get("IoT","port"))

        clientId = "ai4change-yolo-" + uuid.uuid4().hex

        # Configure logging
        logger = logging.getLogger("AWSIoTPythonSDK.core")
        logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

        # Init AWSIoTMQTTClient
        self.myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
        self.myAWSIoTMQTTClient.configureEndpoint(host, port)
        self.myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

        # AWSIoTMQTTClient connection configuration
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    def connect(self):
        self.myAWSIoTMQTTClient.connect()

    def subscribe(self, topic, callback):
        self.myAWSIoTMQTTClient.subscribe(topic, 1, callback)

    def publish(self, topic, message):
        self.myAWSIoTMQTTClient.publish(topic, message, 1)
