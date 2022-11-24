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

try:
    for z in range(55):
        searchQ += searchOps[random.randint(0,len(searchOps)-1)]

    for y in range(len(searchQ)):
        search(searchQ[:y])
    
    notification.notify(title = "Done", message="Rewards Collected")
    
except p.FailSafeException:
    notification.notify(title = "Stopped", message="Execution Stopped")
    
    
    
    
