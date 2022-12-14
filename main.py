# import pyscreenshot as ImageGrab
# import pytesseract
import pyautogui
import pydirectinput
import time
import numpy as np
import BrowserDriver
import math


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


def run():
    # Start running
    pydirectinput.press("=")
    print("Start running")


def stop():
    # Stop running
    pydirectinput.press("=")
    print("Stop running")


def trackplayer(aeternummap):
    currentposition = BrowserDriver.getposition(aeternummap)
    time.sleep(0.2)  # Time between measuring coordinatepoints to make sure there is a measurable difference
    newposition = BrowserDriver.getposition(aeternummap)
    return currentposition, newposition


def adjustmovement(currentposition, newposition, destination):
    currentdegrees = calculatedegrees(currentposition[0], currentposition[1], newposition[0], newposition[1])
    newdegrees = calculatedegrees(newposition[0], newposition[1], destination[0], destination[1])
    degreeoffset = newdegrees - currentdegrees
    pydirectinput.moveRel(degreeoffset, None)
    print("moving mouse ", degreeoffset, " pixels")


# calculate distance between player position and destination
def calculatedistance(playercoordinates, destination):
    return math.hypot(destination[0]-playercoordinates[0], destination[1]-playercoordinates[1])


while True:
    # The route my man supposed to walk(edit this with your route)
    Walkingroute = ((7285.500, 3047.500), (7286.618, 3074.531), (7262.379, 3091.458), (7302.864, 3127.777))

    def start(route):
        aeternummap = BrowserDriver.StartBrowser()
        selectgamewindow()

        for destination in route:
            run()  # Start running
            destinationreached = False
            while not destinationreached:

                # keep track of coordinates
                playercoordinates = trackplayer(aeternummap)

                # Keep player on track
                adjustmovement(playercoordinates[0], playercoordinates[1], destination)

                # Calculate distance left
                distance = calculatedistance(playercoordinates[1], destination)
                print(distance)

                while distance < 5:
                    playercoordinates = trackplayer(aeternummap)
                    distance = calculatedistance(playercoordinates[1], destination)
                    print(distance)
                    if distance < 2:
                        stop()  # Stop running
                        destinationreached = True
                        print("Destination Reached")
                        break

            # Start looting
            pydirectinput.press("F5")
            print("Looting")
            time.sleep(2)

    start(Walkingroute)

time.sleep(2)








