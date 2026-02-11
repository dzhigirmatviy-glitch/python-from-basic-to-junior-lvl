from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_basic_calculator():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        first = driver.find_element(By.ID, "number1Field")
        first.send_keys("5")

        second = driver.find_element(By.ID, "number2Field")
        second.send_keys("3")

        operation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        operation.select_by_visible_text("Add")

        calculate = driver.find_element(By.ID, "calculateButton")
        calculate.click()

        result = driver.find_element(By.ID, "numberAnswerField")
        answer = result.get_attribute("value")

        assert answer == "8"
        print("Test passed! 5 + 3 = 8")
    finally:
        driver.quit()

def test_calculator_subtract():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        first = driver.find_element(By.ID, "number1Field")
        first.send_keys("10")

        second = driver.find_element(By.ID, "number2Field")
        second.send_keys("4")

        operation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        operation.select_by_visible_text("Subtract")

        calculate = driver.find_element(By.ID, "calculateButton")
        calculate.click()

        result = driver.find_element(By.ID, "numberAnswerField")
        answer = result.get_attribute("value")

        assert answer == "6"
        print("Test passed! 10 - 4 = 6")
    finally:
        driver.quit()

def test_calculator_multiply():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        first = driver.find_element(By.ID, "number1Field")
        first.send_keys("10")

        second = driver.find_element(By.ID, "number2Field")
        second.send_keys("10")

        operation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        operation.select_by_visible_text("Multiply")

        calculate = driver.find_element(By.ID, "calculateButton")
        calculate.click()

        result = driver.find_element(By.ID, "numberAnswerField")
        answer = result.get_attribute("value")

        assert answer == "100"
        print("Test passed! 10 * 10 = 100")
    finally:
        driver.quit()

def test_calculator_divide():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        first = driver.find_element(By.ID, "number1Field")
        first.send_keys("1000")

        second = driver.find_element(By.ID, "number2Field")
        second.send_keys("2")

        operation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        operation.select_by_visible_text("Divide")

        calculate = driver.find_element(By.ID, "calculateButton")
        calculate.click()

        result = driver.find_element(By.ID, "numberAnswerField")
        answer = result.get_attribute("value")

        assert answer == "500"
        print("Test passed! 1000 / 2 = 500")

    finally:
        driver.quit()

def test_calculator_concatenate():
    driver = webdriver.Chrome()
    try:
        driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        first = driver.find_element(By.ID, "number1Field")
        first.send_keys("10f")

        second = driver.find_element(By.ID, "number2Field")
        second.send_keys("2b")

        operation = Select(driver.find_element(By.ID, "selectOperationDropdown"))
        operation.select_by_visible_text("Concatenate")

        calculate = driver.find_element(By.ID, "calculateButton")
        calculate.click()
        result = driver.find_element(By.ID, "numberAnswerField")
        answer = result.get_attribute("value")
        assert answer == "10f2b"
        print("Test passed!")
    finally:
        driver.quit()