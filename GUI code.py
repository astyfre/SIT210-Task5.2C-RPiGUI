from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware def
led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

##GUI def
win = Tk()
win.title("LED GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Event Functions
def ledToggle():
	if led1.is_lit:
		led1.off()
		ledButton["text"] = "Turn Blue on"
	else:
		led1.on()
		ledButton["text"] = "Turn Blue off"
		led2.off()
		ledButton2["text"] = "Turn Green on"
		led3.off()
		ledButton3["text"] = "Turn Red on"
		
def ledToggle2():
	if led2.is_lit:
		led2.off()
		ledButton2["text"] = "Turn Green on"
	else:
		led2.on()
		ledButton2["text"] = "Turn Green off"
		led3.off()
		ledButton3["text"] = "Turn Red on"
		led1.off()
		ledButton["text"] = "Turn Blue on"
		
def ledToggle3():
	if led3.is_lit:
		led3.off()
		ledButton3["text"] = "Turn Red on"
	else:
		led3.on()
		ledButton3["text"] = "Turn Red off"
		led2.off()
		ledButton2["text"] = "Turn Green on"
		led1.off()
		ledButton["text"] = "Turn Blue on"
		
def close():
	RPi.GPIO.cleanup()
	win.destroy()

##Widgets
ledButton = Button(win, text = 'Turn Blue on', font = myFont, command = ledToggle, bg = 'bisque2', height = 1, width = 24)
ledButton.grid(row = 0, column = 1)

ledButton2 = Button(win, text = 'Turn Green on', font = myFont, command = ledToggle2, bg = 'bisque2', height = 1, width = 24)
ledButton2.grid(row = 1, column = 1)

ledButton3 = Button(win, text = 'Turn Red on', font = myFont, command = ledToggle3, bg = 'bisque2', height = 1, width = 24)
ledButton3.grid(row = 2, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

win.protocol("WM DELETE WINDOW", close)

win.mainloop()
