import credentials
import network
import time

class Wifi:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        self.wlan.connect(credentials.SSID, credentials.SSID_PASSWORD)
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

