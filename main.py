from machine import Pin, SoftI2C
from lcd_with_i2c import LCD

lcd = LCD(SoftI2C(scl=Pin(1), sda=Pin(0), freq=100000))
lcd.puts("Hello World.")