import subprocess
import time
import pyautogui
import calendar
import sys
from datetime import datetime
from datetime import date

#Stores the current time and day as a string
day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
datetoday = date.today()
daytoday = calendar.day_name[datetoday.weekday()]
print(daytoday)



#Specifies the classes
if daytoday == 'Monday':
    class1 = '07:40' 
    class2 = '09:20'
    class3 = '10:25'
    class4 = '11:15'
    class5 = '12:05'
    class1_sub = 'english literature' 
    class2_sub = 'computer'
    class3_sub = 'chemistry'
    class4_sub = 'physics'
    class5_sub = 'physics'

if daytoday == 'Tuesday':
    class1 = '07:40' 
    class2 = '08:30'
    class3 = '10:25'
    class4 = '11:15'
    class5 = '12:05'
    class1_sub = 'math' 
    class2_sub = 'physics'
    class3_sub = 'english lit'
    class4_sub = 'computer'
    class5_sub = 'physics'

if daytoday == 'Wednesday':
    class1 = '07:40' 
    class2 = '09:20'
    class3 = '10:25'
    class4 = '11:15'
    class5 = '12:05'
    class1_sub = 'physics' 
    class2_sub = 'computer'
    class3_sub = 'chemistry'
    class4_sub = 'math'
    class5_sub = 'physics'

if daytoday == 'Thursday':
    class1 = '01:36'
    class2 = '09:20'
    class3 = '10:25'
    class4 = '11:15'
    class5 = '12:05'
    class1_sub = 'english literature' 
    class2_sub = 'computer'
    class3_sub = 'physics'
    class4_sub = 'chemistry'
    class5_sub = 'math'

if daytoday == 'Friday':
    class1 = '07:40' 
    class2 = '08:30'
    class3 = '09:20'
    class4 = '10:25'
    class5 = '12:05'
    class1_sub = 'chemistry' 
    class2_sub = 'computer'
    class3_sub = 'physics'
    class4_sub = 'english literature'
    class5_sub = 'math'

if daytoday == 'Saturday':
    class1 = '07:40' 
    class2 = '08:30'
    class3 = '09:20'
    class4 = '10:25'
    class5 = '21:41'
    class1_sub = 'physics' 
    class2_sub = 'chemistry'
    class3_sub = 'computer'
    class4_sub = 'math'
    class5_sub = 'english literature' 

if daytoday == 'Sunday':
    sys.exit() 


url = pyautogui.locateOnScreen('imgs/url.png', grayscale=True, confidence=0.5)
sidebar = pyautogui.locateOnScreen('imgs/sidebar.png', grayscale=True, confidence=0.5)
chemistry = pyautogui.locateOnScreen('imgs/chemistry.png', grayscale=True, confidence=0.5)
eng_lang = pyautogui.locateOnScreen('imgs/eng_lang.png', grayscale=True, confidence=0.5)
eng_lit = pyautogui.locateOnScreen('imgs/eng_lit.png', grayscale=True, confidence=0.5)
math = pyautogui.locateOnScreen('imgs/math.png', grayscale=True, confidence=0.5)
physics = pyautogui.locateOnScreen('imgs/physics.png', grayscale=True, confidence=0.5)
computer = pyautogui.locateOnScreen('imgs/computer.png', grayscale=True, confidence=0.5)

#Clicking Different buttons and navigating to the link
while(True):
    print('Running')
    timenow = datetime.now().strftime("%H:%M")

    #Checking which class it is or if we have a class
    if timenow == class1:

        #Opeining the  app
        subprocess.Popen(['open', '-a', '/Applications/Firefox.app/Contents/MacOS/Firefox'])
        pyautogui.hotkey('command', 'ctrlleft', 'option', 'shiftleft', 'f')
    
        #Going to google classroom tab
        pyautogui.hotkey('command', '3')
        pyautogui.moveTo(sidebar)
        pyautogui.click()
        if class1_sub.lower() == 'chemistry':
            pyautogui.moveTo(chemistry)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class1_sub.lower() == 'math':
            pyautogui.moveTo(math)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class1_sub.lower() == 'english language':
            pyautogui.moveTo(eng_lang)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class1_sub.lower() == 'english literature':
            pyautogui.moveTo(eng_lit)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class1_sub.lower() == 'physics':
            pyautogui.moveTo(physics)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class1_sub.lower() == 'computer':
            pyautogui.moveTo(computer)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        break
    
    elif timenow == class2:
        #Opening the  app
        subprocess.Popen(['open', '-a', '/Applications/Firefox.app/Contents/MacOS/Firefox'])
        pyautogui.hotkey('command', 'ctrlleft', 'option', 'shiftleft', 'f')

        #Going to google classroom tab
        pyautogui.hotkey('command', '3')
        pyautogui.moveTo(sidebar)
        pyautogui.click()
        if class2_sub.lower() == 'chemistry':
            pyautogui.moveTo(chemistry)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class2_sub.lower() == 'math':
            pyautogui.moveTo(math)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class2_sub.lower() == 'english language':
            pyautogui.moveTo(eng_lang)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class2_sub.lower() == 'english literature':
            pyautogui.moveTo(eng_lit)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class2_sub.lower() == 'physics':
            pyautogui.moveTo(physics)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class2_sub.lower() == 'computer':
            pyautogui.moveTo(computer)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(810, 894)
            pyautogui.click()
        break
    
    elif timenow == class3:
        #Opeining the  app
        subprocess.Popen(['open', '-a', '/Applications/Firefox.app/Contents/MacOS/Firefox'])
        pyautogui.hotkey('command', 'ctrlleft', 'option', 'shiftleft', 'f')
    
        #Going to google classroom tab
        pyautogui.hotkey('command', '3')
        pyautogui.moveTo(sidebar)
        pyautogui.click()
        if class3_sub.lower() == 'chemistry':
            pyautogui.moveTo(chemistry)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class3_sub.lower() == 'math':
            pyautogui.moveTo(math)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class3_sub.lower() == 'english language':
            pyautogui.moveTo(eng_lang)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class3_sub.lower() == 'english literature':
            pyautogui.moveTo(eng_lit)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class3_sub.lower() == 'physics':
            pyautogui.moveTo(physics)
            pyautogui.click()
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class3_sub.lower() == 'computer':
            pyautogui.moveTo(computer)
            pyautogui.click()
            pyautogui.moveTo(url)
            pyautogui.click() 
        break

    elif timenow == class4:
        #Opeining the  app
        subprocess.Popen(['open', '-a', '/Applications/Firefox.app/Contents/MacOS/Firefox'])
        pyautogui.hotkey('command', 'ctrlleft', 'option', 'shiftleft', 'f')

        #Going to google classroom tab
        pyautogui.hotkey('command', '3')
        pyautogui.moveTo(sidebar)
        pyautogui.click()
        if class4_sub.lower() == 'chemistry':
            pyautogui.moveTo(chemistry)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class4_sub.lower() == 'math':
            pyautogui.moveTo(math)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class4_sub.lower() == 'english language':
            pyautogui.moveTo(eng_lang)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class4_sub.lower() == 'english literature':
            pyautogui.moveTo(eng_lit)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class4_sub.lower() == 'physics':
            pyautogui.moveTo(physics)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class4_sub.lower() == 'computer':
            pyautogui.moveTo(computer)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()   
        break
    
    elif timenow == class5:
        #Opeining the  app
        subprocess.Popen(['open', '-a', '/Applications/Firefox.app/Contents/MacOS/Firefox'])
        pyautogui.hotkey('command', 'ctrlleft', 'option', 'shiftleft', 'f')
    
        #Going to google classroom tab
        pyautogui.hotkey('command', '3')
        pyautogui.moveTo(sidebar)
        pyautogui.click()
        if class5_sub.lower() == 'chemistry':
            pyautogui.moveTo(chemistry)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class5_sub.lower() == 'math':
            pyautogui.moveTo(math)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class5_sub.lower() == 'english language':
            pyautogui.moveTo(eng_lang)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class5_sub.lower() == 'english literature':
            pyautogui.moveTo(eng_lit)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class5_sub.lower() == 'physics':
            pyautogui.moveTo(physics)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()
        elif class5_sub.lower() == 'computer':
            pyautogui.moveTo(computer)
            pyautogui.click()
            #time.sleep(3)
            pyautogui.moveTo(url)
            pyautogui.click()  
        break
