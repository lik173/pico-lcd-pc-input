from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
import machine
import io
import utime


def help():
    lcd.putstr("@cls\nClear screen")
    utime.sleep(2)
    lcd.clear()
    lcd.putstr("@backlight\non/off")
    utime.sleep(2)
    lcd.clear()
    lcd.putstr("@cursor\non/off")
    utime.sleep(2)
    lcd.clear()
    lcd.putstr("@lcd\non/off")
    utime.sleep(2)
    lcd.clear()
    lcd.putstr("@cursorblink\non/off")
    utime.sleep(2)
    lcd.clear()
    lcd.putstr("@help\nHelp")
    utime.sleep(2)
    lcd.clear()
    
 
 

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)



conversion_factor = 3.3 / (65535)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    
    text = input("Text: ")
    
    
    
    
    
    if (text == "@cls"):
        lcd.clear()
        text = input("Text: ")
    if (text == "@n"):
        lcd.putchar('\n')
        text = input("Text: ")
    if (text == "@backlight on"):
        lcd.backlight_on()
        text = input("Text: ")
    if (text == "@backlight off"):
        lcd.backlight_off()
        text = input("Text: ")
    if (text == "@lcd on"):
        lcd.display_on()
        text = input("Text: ")
    if (text == "@lcd off"):
        lcd.display_off()
        text = input("Text: ")
    if (text == "@cursor on"):
        lcd.show_cursor()
        text = input("Text: ")
    if (text == "@cursor off"):
        lcd.hide_cursor()
        text = input("Text: ")
    if (text == "@cursorblink on"):
        lcd.blink_cursor_on()
        text = input("Text: ")
    if (text == "@cursorblink of"):
        lcd.blink_cursor_off()
        text = input("Text: ")
    if (text == "@help"):
        lcd.clear()
        help()
        text = input("Text: ")
        
    lcd.putstr(text)
    



