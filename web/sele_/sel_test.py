from selenium import webdriver

driver = webdriver.Chrome('/Users/choopick_mac/Desktop/coding/chromedriver')

driver.get('https://codeit.kr')
driver.quit()