
from selenium import webdriver
from selenium.webdriver.common.by import By


def start_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument(r"--user-data-dir=C:\Users\falco\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(r"C:\Users\falco\AppData\Roaming\JetBrains\PyCharmCE2022.3\scratches\Chromedriver", options =options)
    driver.get('https://aeternum-map.gg/')
    return driver


def get_position(driver):
    raw_coordinates = driver.find_element(By.CLASS_NAME, "leaflet-bottom.leaflet-right").text
    raw_coordinates = raw_coordinates.translate({ord(c): None for c in '[]'})

    # split in case user used mouse on the map which sends mouse coordinates and select playermovement index
    position = raw_coordinates.splitlines()
    if len(position) > 1:
        position.pop(0)

    splitted_coordinates = position[0].split(",")
    coordinates = [float(x) for x in splitted_coordinates] # [round(float(x)) for x in splitted_coordinates]
    return coordinates




