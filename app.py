from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.xe.com/currencyconverter/")



amount = driver.find_element_by_id("amount")
amount.clear()
amount.send_keys(input("Enter your valueu(USD to EUR):"))

submit = driver.find_element_by_xpath("//*[@id='converterForm']/form/button[2]")
submit.click()