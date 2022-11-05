import time
import logging
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException

logging.basicConfig(filename='RandomBotLogger.log', level=logging.INFO)
LOGGER = logging.getLogger()
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s–%(name)s– %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
consoleHandler.setFormatter(formatter)
LOGGER.addHandler(consoleHandler)

driver = webdriver.Firefox()
driver.get("http://localhost:3000")

class Tags():
    square1 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[1]"
    square2 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[2]"
    square3 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[3]"
    square4 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[4]"
    square5 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[5]"
    square6 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[6]"
    square7 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[7]"
    square8 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[8]"
    square9 = "(//div[contains(@class, 'board-row')]//button[contains(@class, 'square')])[9]"
    winner = "//div[contains(@class, 'game-info')]//div[contains(text(), 'Winner:')]"
    tie = "//div[contains(@class, 'game-info')]//div[contains(text(), 'tie')]"

def playTTT():

    squares = [Tags.square1,Tags.square2,Tags.square3,
               Tags.square4,Tags.square5,Tags.square6,
               Tags.square7,Tags.square8,Tags.square9]

    random_square = randint(0,8)
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, Tags.winner).is_displayed()
        text = driver.find_element(By.XPATH, Tags.winner).text
        LOGGER.info(str(text))
        driver.save_screenshot("screenshot.png")
        driver.close()
    except NoSuchElementException:
        pass
    try:
        driver.find_element(By.XPATH, Tags.tie).is_displayed()
        LOGGER.info("Tie")
        driver.save_screenshot("screenshot.png")
        driver.close()
    except NoSuchElementException:
        pass

    try:
        for i in range(len(squares)):
            text = driver.find_element(By.XPATH, squares[random_square]).text
            if text == 'O':
                LOGGER.info("Square " + str(random_square) + " marked by O.")
                break
            elif text == 'X':
                LOGGER.info("Square " + str(random_square) + " already marked by X.")
                break
            else:
                element = driver.find_element(By.XPATH, squares[random_square])
                element.click()
                LOGGER.info("Clicking square:" + str(random_square))
                break
        playTTT()
    except InvalidSessionIdException:
        pass

if __name__=='__main__':
    playTTT()
