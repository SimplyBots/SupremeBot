from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def openSupreme():
    browser = webdriver.Chrome(executable_path=r"C:\Users\Owner\Downloads\chromedriver_win32\chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser.get("https://www.supremenewyork.com/shop/all")

    jackets = browser.find_element_by_link_text("jackets")
    jackets.click()

    jacketType = "Curve Track Jacket"
    jacketColour = "White"

    WebDriverWait(browser, 1).until( EC.presence_of_element_located((By.LINK_TEXT, jacketType)) )
    ActionChains(browser).click(browser.find_element_by_link_text(jacketType)).perform()

    browser.find_elements_by_xpath("//*[contains(text(), " + jacketColour + ")]")[0].click()
    WebDriverWait(browser, 1.7).until( EC.presence_of_element_located((By.NAME, "commit")) )

    submit_element = browser.find_element_by_name("commit")
    ActionChains(browser).click(submit_element).perform()

    sleep(0.8)
    checkout = browser.find_element_by_link_text("checkout now")
    ActionChains(browser).click(checkout).perform()

    sleep(1)
    cardinal_order = browser.find_element_by_name("cardinal_order_no").get_attribute("value")
    print(cardinal_order)