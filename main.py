import pyautogui as pt 
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("clip.jpg", confidence =.6)
x = position1[0]
y = position1[1]


# Gets messages 
def get_message():
	global x,y

	position1 = pt.locateOnScreen("clip.jpg", confidence =.6)
	x = position1[0]
	y = position1[1]
	pt.moveTo(x, y, duration=.5)
	pt.moveTo(x + 40, y - 70, duration =.5)


	get_message()
