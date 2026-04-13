from machine import Pin, SoftI2C, 
from lcd_with_i2c import LCD
import network, wifi


lcd = LCD(SoftI2C(scl=Pin(1), sda=Pin(0), freq=100000))
lcd.puts("Hello World.")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi.ssid, wifi.password)

