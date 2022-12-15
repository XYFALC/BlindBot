import pyautogui
import pydirectinput
import time
import numpy as np
import blindbot.browserdriver as browserdriver
import math


# select the game window
def select_gamewindow():
    newworld_window = pyautogui.getWindowsWithTitle("New World")
    for window in newworld_window:
        if window.title == "New World":
            newworld_window = window
            break
    pyautogui.press('space ')
    newworld_window.activate()
    center_w = round(newworld_window.left + (newworld_window.width/2))
    center_h = round(newworld_window.top + (newworld_window.height/2))
    pydirectinput.moveTo(center_w, center_h)
    pydirectinput.click()


# calculate degrees using current player position and destination
def calculate_degrees(x1, y1, x2, y2):
    degrees = np.arctan2(x2 - x1, y2 - y1)*180/np.pi
    if degrees < 0:
        degrees += 360
    return round(degrees)


def run():
    # Start running
    pydirectinput.press("=")
    print("Start running")


def stop():
    # Stop running
    pydirectinput.press("=")
    print("Stop running")


def track_player(aeternum_map):
    current_position = browserdriver.get_position(aeternum_map)
    # Time between measuring coordinatepoints to make sure there is a measurable difference
    time.sleep(0.2)
    new_position = browserdriver.get_position(aeternum_map)
    return current_position, new_position


def adjust_movement(current_position, new_position, destination):
    current_degrees = calculate_degrees(
        current_position[0], current_position[1], new_position[0], new_position[1])
    new_degrees = calculate_degrees(
        new_position[0], new_position[1], destination[0], destination[1])
    degree_offset = new_degrees - current_degrees
    pydirectinput.moveRel(degree_offset, None)
    print("moving mouse ", degree_offset, " pixels")


# calculate distance between player position and destination
def calculate_distance(player_coordinates, destination):
    return math.hypot(destination[0] - player_coordinates[0], destination[1] - player_coordinates[1])


while True:
    # The route my man supposed to walk(edit this with your route)
    walking_route = ((9718.066, 3003.621), (9743.861, 3035.369), (9743.861, 3035.369),
                     (9754.434, 3018.725), (9761.420, 3025.093), (9763.248, 3032.627))

    def start(route):
        aeternum_map = browserdriver.start_browser()
        select_gamewindow()
        time.sleep(3)  # wait for game window to open
        for destination in route:
            run()  # Start running
            destination_reached = False
            while not destination_reached:

                # keep track of coordinates
                player_coordinates = track_player(aeternum_map)

                # Keep player on track
                adjust_movement(
                    player_coordinates[0], player_coordinates[1], destination)

                # Calculate distance left
                distance = calculate_distance(
                    player_coordinates[1], destination)
                print(distance)

                while distance < 5:
                    player_coordinates = track_player(aeternum_map)
                    distance = calculate_distance(
                        player_coordinates[1], destination)
                    print(distance)
                    if distance < 2:
                        stop()  # Stop running
                        destination_reached = True
                        print("Destination Reached")
                        break

            # Start looting
            time.sleep(1)
            pydirectinput.press("F5")
            print("Looting")
            # TODO: check if current object is looted
            # TODO: Remove timebreaks(time.sleep(10)) where possible to optimize the bot
            # TODO: Create checkpoints for randomization, not every destination has to be a lootable object
            time.sleep(10)

    start(walking_route)

time.sleep(200)
