import time
import logging
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException

LOGGER = logging.getLogger(__name__)
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
    ohSquare = "//div[contains(@class, 'board-row')]//button[contains(text(), 'O')]"
    winner = "//div[contains(@class, 'game-info')]//div[contains(text(), 'Winner:')]"
    tie = "//div[contains(@class, 'game-info')]//div[contains(text(), 'tie')]"

def playTTT():

    squares = [Tags.square1,Tags.square2,Tags.square3,
               Tags.square4,Tags.square5,Tags.square6,
               Tags.square7,Tags.square8,Tags.square9]

    clickedSquares = []
    random_square = randint(0,8)
    time.sleep(5)

    if not clickedSquares:
        LOGGER.debug("I made it into the first if statement")
        element = driver.find_element(By.XPATH, squares[random_square])
        element.click()
        clickedSquares.append(random_square)

    try:
        driver.find_element(By.XPATH, Tags.winner).is_displayed()
        text = driver.find_element(By.XPATH, Tags.winner).text
        print(str(text))
        driver.close()
    except NoSuchElementException:
        pass
    try:
        driver.find_element(By.XPATH, Tags.tie).is_displayed()
        print("Tie")
        driver.close()
    except NoSuchElementException:
        pass

    try:
        for i in range(0,9):
            if squares[i] == Tags.ohSquare:
                clickedSquares.append(i)

        for i in clickedSquares:
            LOGGER.debug("I made it into the second for loop")
            if i == random_square:
                LOGGER.debug("I made it into the second if statement")
                playTTT()
            else:
                LOGGER.debug("I made it into the first else statement")
                clickedSquares.append(random_square)
        
        element = driver.find_element(By.XPATH, squares[random_square])
        element.click()
    except InvalidSessionIdException:
        pass

if __name__=='__main__':
    playTTT()