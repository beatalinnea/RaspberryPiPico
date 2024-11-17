import machine
from machine import Pin
import utime as time
from dht import DHT11
from wifi import Wifi
from MQTTManager import MQTTManager
import ujson

# Set publish variables
last_publish = time.time()
publish_interval = 60

# Initialize LED
led = Pin("LED", Pin.OUT)
# led.on()

# Connect to WiFi
wifi = Wifi()
wifi.connect()

# if PicoW Failed to connect to MQTT broker. Reconnecting...'
def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()

# Callback function to handle messages
def sub_cb(topic, msg):
    msg = msg.decode('utf-8')
    if msg == "ON":
        led.value(1)
    elif msg == "OFF":
        led.value(0)


# The GPIO number is 13 which is equal to the pin number 17
pin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

def main():
    print(f"Begin connection with MQTT Broker")
    # Initialize and connect to MQTT
    mqtt_manager = MQTTManager()
    client = mqtt_manager.connect()
    mqtt_manager.subscribe("led", sub_cb)
    while True:
        client.check_msg()  # Check for new messages and call the callback function
        global last_publish
        if (time.time() - last_publish) >= publish_interval:
            try:
                t = sensor.temperature
                time.sleep(2)
                h = sensor.humidity
            except:
                print("An exception occurred")  
                continue  
            print("Temperature: {}".format(t))
            print("Humidity: {}".format(h))
            try: 
                # Publish to Adafruit IO
                temp_data_json = ujson.dumps({"value": t})
                humid_data_json = ujson.dumps({"value": h})
                mqtt_manager.publish("temperature", temp_data_json)
                mqtt_manager.publish("humidity", humid_data_json)

                # publish as json
                json = mqtt_manager.prepare_data(t, h)
                mqtt_manager.publish("sensor_data", json)
                last_publish = time.time()
                print("Sent to adafruit")
            except Exception as e:
                print("An exception occurred during publishing:", e)

if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()