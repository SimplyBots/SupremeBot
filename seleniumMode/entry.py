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

    jacketType = "name-link"
    jacketColour = "Black"

    WebDriverWait(browser, 1.5).until( EC.presence_of_element_located((By.CLASS_NAME, jacketType)) )
    browser.find_elements_by_xpath("//*[contains(text(), " + jacketType + ")]")
    browser.find_elements_by_xpath("//*[contains(text(), " + jacketColour + ")]")[0].click()
    WebDriverWait(browser, 2).until( EC.presence_of_element_located((By.NAME, "commit")) )

    submit_element = browser.find_element_by_name("commit")
    ActionChains(browser).click(submit_element).perform()

    while True:
        print("")