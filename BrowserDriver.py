
from selenium import webdriver
from selenium.webdriver.common.by import By


def StartBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument(r"--user-data-dir=C:\Users\falco\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(r"C:\Users\falco\AppData\Roaming\JetBrains\PyCharmCE2022.3\scratches\Chromedriver", options =options)
    driver.get('https://aeternum-map.gg/')
    return driver


def getposition(driver):
    rawcoordinates = driver.find_element(By.CLASS_NAME, "leaflet-bottom.leaflet-right").text
    rawcoordinates = rawcoordinates.translate({ord(c): None for c in '[]'})

    # split in case user used mouse on the map which sends mouse coordinates and select playermovement index
    position = rawcoordinates.splitlines()
    if len(position) > 1:
        position.pop(0)

    splittedcoordinates = position[0].split(",")
    coordinates = [float(x) for x in splittedcoordinates]
    # coordinates = [round(float(x)) for x in splittedcoordinates]
    return coordinates




