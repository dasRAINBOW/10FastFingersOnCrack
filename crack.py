import cv2
import mss
import numpy
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
firstRun = True

def normMode():
    global firstRun
    sleep(3)
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(im)
            # print(text)
            if firstRun == True:
                textOld = text

            if text == textOld and firstRun == False:
                quit()

            pyautogui.typewrite(text + " ", 0.014)
            firstRun = False
            textOld = text

def specialMode():
    sleep(1)
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(im)
            text = text.strip().replace("\n", " ")
            splitText = text.split()
            dele = 0
            for i in range(len(splitText)):
                word = splitText[i - dele]
                if word not in splitContent:
                    del splitText[i - dele]
                    dele += 1
            for e in range(len(splitText)):
                text += splitText[e] + " "
            pyautogui.typewrite(text, 0.012)
            with pyautogui.hold('tab'):
                pyautogui.press('enter')
            exit()

def devMode():
    print("Nothing to see here :\\")
    sleep(3)
        
with open('english.txt', encoding="utf8") as f:
    contents = f.read()
    splitContent = contents.split()

mode = input("Norm = 1; Comp = 2; Bypass = 3; ")

if mode == str(1):
    mon = {'top': 225, 'left': 435, 'width': 1000, 'height': 60}
    normMode()
elif mode == str(2):
    mon = {'top': 190, 'left': 440, 'width': 880, 'height': 60}
    normMode()
elif mode == str(3):
    mon = {'top': 250, 'left': 580, 'width': 600, 'height': 200}
    specialMode()
elif mode == "das":
    mon = {'top': 250, 'left': 580, 'width': 600, 'height': 200}
    print("Dev mode enabled!")
    devMode()
