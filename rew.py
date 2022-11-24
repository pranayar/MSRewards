import pyautogui as p
import time
import random
from plyer import notification

def search(query):
    p.hotkey("ctrl","e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.67)
    

time.sleep(2)
searchOps = "qwertyuiopasdfghjklzxcvbnm1234567890!\"£$%^&*()/-+.|¬`[];'#,/{}:@~<>?"
searchQ = ""

for z in range(2):
    searchQ += searchOps[random.randint(0,len(searchOps)-1)]

for y in range(len(searchQ)):
    search(searchQ[:y])
    
    
notification.notify(title = "Done", message="Rewards Collected")