# Assignment - Internet of Things

## A Learning Adventure with Raspberry Pi Pico
Beata Eriksson - be222gr

In this project I've had my first encounter with a Raspberry Pi Pico and a DHT11 sensor. This project includes a fritzing design for connections between the Raspberry Pi Pico and the DHT11 sensor, as well as my code that runs on the Pico to measure both temperature and humidity through the sensor and send it to Adafruit for data collection and visualization.

As for me - starting from scratch regarding hardware knowledge and with no familiarity with Python or MicroPython (but being a programmer in other languages) - following this project and implementing it yourself might take a full working week or so, to dive in to all tech specifications, the set up and connections, and to build and visualize your data.

## Tutorial on how to build a temperature and humidity sensor

### Objective

I've chosen to build this device to read the humidity and temperature in my home office environment. By doing this, I learned about the Raspberry Pi Pico W and MicroPython. I got to know more about Internet of Things including how to implement, use and build IoT projects myself. Through my code, hardware and connections I am now able to measure and collect data about my home environment, which opens up unlimited possibilities for building software around it.

### Material

> Material:
>| IoT Thing | Explanation      | Price           |
>| --------- | ---------------- |---------------- |
>| Raspberry Pi Pico WH | Microcontroller, the main component | 109 SEK |
>| Breadboard | For placing the pico, sensor and wires for connection without soldering| 69 SEK |
>| Jumper wires - male/male | For making connections mentioned above | 29 SEK |
>| DHT11 | Sensor for measuring temperature and humidity | 39 SEK |
>| Micro USB cable | Powering the Pico from a computer | Probably free |

In this project, I have chosen to work with the Raspberry Pi Pico WH, as seen below. It's a tiny microcontroller that's a great choice for a first interaction with IoT. I chose the soldered model to easily use and connect with my sensor using wires and a breadboard.
              
![pico!](https://www.electrokit.com/cache/ba/700x700-product_41019_41019114_PICO-WH-HERO.jpg)              
Raspberry Pi Pico WH. electrokit.com.
              
I used a breadboard for creating connections between my sensor and my pico. This is a very stable way and requires no soldering.              
![breadboard!](https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg)              
Breadboard. electrokit.com.              

Male/male jumper wires for connecting the Pico and sensor. Ended up needing 3. They came in a pack of more.              
![wires!](https://www.electrokit.com/upload/product/41012/41012909/41012909.jpg)              
Jumper wires. electrokit.com.              

Temperature/humidity sensor DHT11 (without resistor). With this, I had to be sure to connect to the correct 3.3V output pin on my Pico. By doing this, I did not need a resistor to control the input voltage to my sensor to avoid burning it.
![dht11!](https://www.electrokit.com/upload/product/41016/41016231/41016231.jpg)
DHT11. electrokit.com.

### Computer setup

> #### Starting up the pico
> First thing I had to do was to flash the firmware on my Pico to run MicroPython. This is done by first connecting the micro USB to the Pico, then holding the 'BOOTSEL' button down on my Pico - and while holding, plug in the USB (other end of the cable) to my computer. The Pico will then show up as a mass storage device called "RPI-RP2" on my desktop, and you release the button. After that, I dragged the UF2 file found [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) to the Pico on my desktop. A note here is that if you're using a Mac, you might find that after downloading the file, you are not able to read it and therefore can't drag and drop it to your Pico. I needed to do this through my terminal by running: ``cp /Users/Beata/Desktop/RPI_PICO_W-20240222-v1.22.2.uf2 /Volumes/RPI-RP2``. As soon as the file is added correctly to the Pico, it will disappear from the desktop and reboot.
> #### Python
> I needed to install Python on my computer. This was simply done through the Python official website.
> #### IDE
> I chose Visual Studio Code as my IDE. To adapt my VS Code to this particular project, I needed to install the plugin MicroPico (Pico-W-Go). This extension helped me easily see when my Raspberry Pi Pico W was connected or not, and to upload and run my project and files to the pico. 
> #### Uploading and running code
> The code is written in MicroPython. Using the MicroPico extension, it was easy to add my current project to my Pico, then run my main file on the Pico. This was done with the extension providing buttons for these options in my IDE. Now I could program as usual - just don't forget to upload updates to the pico. Initially, I used logs to check that my code was running correctly.
> #### Encountered Troubles
> When using the tool "Toggle Pico-W-FS" by MicroPico, I noticed my workspace in my IDE changed to being one step above from the project I was working in. This created issues when adding the project to the Pico and running it - while being in the workspace and not directly in my project. This caused my Pico to fully freeze. I then needed to reset the flash memory, following the documentation at the bottom of [this page](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#raspberry-pi-pico-w-and-pico-wh). This was done with the same procedure as mentioned above when starting up: holding the 'BOOTSEL' button while plugging in, then moving the nuke flash UF2 file to the Pico, then flashing the firmware once again as done initially.


### Putting everything together

Below is my design for connecting the sensor with my Raspberry Pi Pico WH on the breadboard using jumper wires. What I noticed as an IoT rookie is that I had to push the Pico quite hard into the breadboard. It's also important to understand how the breadboard is connected per row. This must be done following the documentation for the devices being used. The first pin on the DHT11 is the voltage supply - here connected to the 3.3V output pin on my Pico. This was necessary since I am not using a resistor and don't want to burn my sensor by giving it too high voltage. The second pin on my DHT11 is for the data, and I am connecting it to output pin GPIO13, but there are several more to choose from as you can see on the chart for the Pico pins. This enables the data to be sent from the sensor to the Pico. The third pin on the DHT11 is not relevant, and the fourth one is the ground pin, which should be connected to a GND (ground) pin on the Pico. This is needed to complete the circuit and is crucial to make the electrical flow work between the Pico and the DHT11.              
![fritzing!](/media/img/fritzing.png)

### Platform

I am using a free platform called Adafruit to visualize my data. In Adafruit, you can create "feeds" to which you can send and recieve data/messages. Adafruit has a built-in dashboard function where you can choose to visualize the data that you choose to send to your feeds. I make sure to have written code so that my Pico is connected to my Wi-Fi, and then can make requests to Adafruit by publishing to a created feed when submitted together with my user credentials. On my Adafruit dashboard, I've also chosen to create a button which is connected to a feed called "led". When this button is clicked, my Pico will instead subscribe, or listen to, when this feed has a change, which will contain either the message "on" or "off". By that, it will then act to turn on or off the device's LED. I send my humidity and temperature data as JSON to separate feeds to be able to use the built-in dashboard functions correctly. I am also sending the data as a combined JSON object, which can be used if you were to build a separate frontend and want to fetch the data from Adafruit. In that case, you could call that specific feed to recieve the JSON containing both the temperature and humidity data.

### The code

I have a main file that is calling methods from other classes in different files. I've tried to keep a neat and separated file structure (SoC). I will show an example of my file handling the Wi-Fi connection - which is then being called in my main file.               

```python=
import network
import time

class Wifi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        SSID = "wifi_name"
        SSID_PASSWORD = "wifi_password"
        self.wlan.connect(SSID, SSID_PASSWORD)
        print(self.wlan.isconnected())

        wait = 5
        while wait > 0:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            wait -= 1
            print('waiting for connection...')
            time.sleep(1)

        if self.wlan.status() != 3:
            raise RuntimeError('wifi connection failed')
        else:
            print('connected')
            ip = self.wlan.ifconfig()[0]
            print('network config: ', ip)
            return ip

# This is how I connect to my Wi-Fi. I have a timer for it so it does not try forever. If there is an issue connecting it will raise an error, if it is in the process of connecting it while count down the timer, if the connectino succeeded the IP-adress and a message will be printed.
```

### Data flow / Connectivity

- I am sending my data once every 60 seconds to Adafruit. I am keeping track of the latest reading with my sensor to ensure it is sent every 60 seconds.
- This data is sent to Adafruit through Wi-Fi connection.
- The communication is done using the MQTT protocol, and I am using the umqttsimple.py file for publish and subscribe methods.
- Using the publish/subscribe model with data being sent in JSON format to Adafruit, this is prepared and sent after each reading from the sensor and therefore being done once every minute.


### Presenting the data

My Adafruit dashboard is available [here](https://io.adafruit.com/be222gr/dashboards/pico).
The temperature and humidity data that is displayed represents the latest sent data. The graphs for each feed show the temperature and humidity data for the last 30 days. When my Pico is connected and running, data from the sensor is sent every 60 seconds.               
![dashboard!](/media/img/dashboard.png)

### Final Thoughts

This truly was a learning adventure! It was my first interaction with IoT from this perspective, and I thoroughly enjoyed it. I heavily relied on Neda's videos, although not everything was accurate for helping me with this specific assignment, they were much needed to follow along some sort of "tutorial". It helped me understand what I was doing and even dare to explore a new field in computer science. I'm grateful for this course and the experience with IoT. Now that I know more about wires and devices, I feel less afraid of them.                

![pico!](/media/img/pico.jpg)              
              
Ensuring everything is in order! Logging. It's working!              
![output!](/media/img/output.png)              

Demo video showcasing my setup and blinking LED.              
![](/media/demo.mp4)              
