from machine import Pin, SoftI2C, 
from lcd_with_i2c import LCD
from time import sleep
import network, wifi


lcd = LCD(SoftI2C(scl=Pin(1), sda=Pin(0), freq=100000))
lcd.puts("Hello World.")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi.ssid, wifi.password)

print()
time_waiting = 0
while wlan.status() != 3:
    print(f"\rWaiting for wifi: {time_waiting} seconds", end="")
    time_waiting = time_waiting + 1
    sleep(1)

