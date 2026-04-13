from machine import Pin, SoftI2C, 
from lcd_with_i2c import LCD
from time import sleep
import network, wifi, ntptime, time


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

time_not_set = True
while time_not_set:
    try:
        ntptime.settime()
    except OSError:
        continue
    else:
        time_not_set = False

while True:
    (Y, M, D, h, m, s, u, u2) = time.localtime(time.time()-21600)
    lcd.clear()
    lcd.puts(f"{h:02}:{m:02}:{s:02}", x=0, y=0)
    lcd.puts(f"{Y}-{M:02}-{D:02}", x=0, y=3)
    sleep(1)
