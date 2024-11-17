import credentials
from umqttsimple import MQTTClient
import ujson

class MQTTManager:
    def __init__(self):
        self.client_id = credentials.CLIENT_ID
        self.client = MQTTClient(credentials.CLIENT_ID, credentials.MQTT_BROKER, credentials.PORT, credentials.ADAFRUIT_USERNAME, credentials.ADAFRUIT_PASSWORD, keepalive=60)

    def connect(self):
        self.client.connect()
        return self.client
    
    # Make it possible to publish data to two different feeds
    def publish(self, feed, data):
        topic = "{}/feeds/{}".format(credentials.ADAFRUIT_USERNAME, feed)
        self.client.publish(topic, str(data).encode())
    
    # Prepare data for different feeds in json format 
    def prepare_data(self, temperature, humidity):
        data = {"feeds": {
            "temperature": temperature, 
            "humidity": humidity}
        }
        return ujson.dumps(data)


    # Set Pico on On or OFF
    def subscribe(self, feed, callback):
        topic = "{}/feeds/{}".format(credentials.ADAFRUIT_USERNAME, feed)
        self.client.set_callback(callback)
        self.client.subscribe(topic)
