# import pyscreenshot as ImageGrab
# import pytesseract
import pyautogui
import pydirectinput
import time
import numpy as np
import BrowserDriver
import math

# some vars
oldposition = [0, 0]


# select the game window
def selectgamewindow():
    newworldwindow = pyautogui.getWindowsWithTitle("New World")
    for window in newworldwindow:
        if window.title == "New World":
            newworldwindow = window
            break
    pyautogui.press('space ')
    newworldwindow.activate()
    centerw = round(newworldwindow.left + (newworldwindow.width / 2))
    centerh = round(newworldwindow.top + (newworldwindow.height / 2))
    pydirectinput.moveTo(centerw, centerh)
    pydirectinput.click()


# calculate degrees using current player position and destination
def calculatedegrees(x1, y1, x2, y2):
    degrees = np.arctan2(x2 - x1, y2 - y1) * 180 / np.pi
    if degrees < 0: degrees += 360
    return round(degrees)


# calculate degrees using current player position and destination
def calculatedegreesOverload(x1, y1, destination):
    degrees = np.arctan2(destination[0] - x1, destination[1] - y1) * 180 / np.pi
    if degrees < 0: degrees += 360
    return round(degrees)


# calculate distance between player position and destination
def calculatedistance(x1, y1, x2, y2):
    return math.hypot(x2-x1, y2-y1)


# caclulate which way in degrees the player is facing
def calculatestartingdegrees(currentposition, coordinatemap):
    time.sleep(0.5)
    pydirectinput.press("=")
    time.sleep(0.5)
    pydirectinput.press("=")
    newposition = BrowserDriver.getposition(coordinatemap)
    startingdegree = calculatedegrees(currentposition[0], currentposition[1], newposition[0], newposition[1])
    return startingdegree


while True:
    # The route my man supposed to walk(edit this with your route)
    route = ((7285.611, 3047,586), (7287.975, 3074,510))

    def recalibrate(previousposition, destination, coordinatemap):
        newposition = BrowserDriver.getposition(coordinatemap)
        currentdegrees = calculatedegrees(previousposition[0], previousposition[1], destination[0], destination[1])
        degreetowalk = calculatedegrees(newposition[0], newposition[1], destination[0], destination[1])
        degreeoffset = degreetowalk - currentdegrees
        pydirectinput.moveRel(degreeoffset, None)
        print("moving mouse ", degreeoffset)

    def start(routetowalk):
        coordinatemap = BrowserDriver.StartBrowser()
        selectgamewindow()

        # For each checkpoint in the given route
        for destination in routetowalk:
            # start running to destination
            pydirectinput.press("=")

            destinationreached = False
            while not destinationreached:
                currentpos = BrowserDriver.getposition(coordinatemap)
                # coordinatieafstand tussen currentpos en destination is te kort misschien? calibreren.
                previousposition = currentpos
                distance = calculatedistance(currentpos[0], currentpos[1], destination[0], destination[1])
                print(distance, " meters left ")

                #reposition camera
                recalibrate(previousposition, destination, coordinatemap)

                while distance < 3:
                    while distance > 1:
                        currentpos = BrowserDriver.getposition(coordinatemap)
                        distance = calculatedistance(currentpos[0], currentpos[1], destination[0], destination[1])
                        print(distance)
                        if distance < 1:
                            pydirectinput.press("=")
                            destinationreached = True
                            print("Destination Reached")

            # Loot the object
            print(BrowserDriver.getposition(coordinatemap))
            print(calculatedistance(currentpos[0], currentpos[1], destination[0], destination[1]))
            pydirectinput.press("F5")
            print("Looting that shit")
            time.sleep(20)

    start(route)

time.sleep(2)








