# pico-lcd-pc-input
That program provides input text and draw it on HD44780 LCD  
  
# System requirements (_tested_)
Raspberry Pi Pico  
MicroPython firmware  
i2c HD44780 LCD (_16x2 tested_)  
Way to connect LCD to RPI Pico  
Something like Thonny IDE  
  
# Using
Load files in your RPI Pico  
Run main.py  
In shell (Thonny) you will get message: {Text: }  
Type any text to display it  
  
# Using without Thonny
You can use that without thonny, but you need to install wsl and any distro
Installing:  
sudo apt install minicom  
minicom -D /dev/ttyS<<COM Number>>
# Change start message
in main.py before while(true) cycle you will see lcd.putstr()  
  
# Commands (_commands starts from "@" symbol_)
@cls - Clear screen  
@n - Next line  
@backlight (on/off) - Back light in your display  
@lcd (on/off) - Turn (on/off) your display  
@cursor (on/off) - Turn (on/off) cursor on display  
@cursorblink (on/off) - Turn (on/off) cursor blink  
@help - Display commands  
