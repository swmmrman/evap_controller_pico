from machine import Pin, SoftI2C, Timer
from lcd_with_i2c import LCD
from time import sleep
import network, wifi, ntptime, time


lcd = LCD(SoftI2C(scl=Pin(1), sda=Pin(0), freq=100000))
lcd.puts("Hello World.")

def show_time(isr):
    global lcd
    (Y, M, D, h, m, s, u, u2) = time.localtime(time.time()-21600)
    lcd.clear()
    lcd.puts(f"{h:02}:{m:02}:{s:02}", x=0, y=0)
    lcd.puts(f"{Y}-{M:02}-{D:02}", x=0, y=3)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi.ssid, wifi.password)

lcd.clear()
time_waiting = 0
while wlan.status() != 3:
    
    lcd.puts("Waiting for wifi:", x=0 ,y=0)
    lcd.puts(f"{time_waiting} seconds", x=0, y=1)
    time_waiting = time_waiting + 1
    sleep(1)

lcd.clear()
lcd.puts("Setting clock")
time_not_set = True
while time_not_set:
    try:
        ntptime.settime()
    except OSError:
        continue
    else:
        time_not_set = False

clock_timer = Timer()
clock_timer.init(freq=1, callback=show_time)