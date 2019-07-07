import time
from selenium import webdriver

driver = webdriver.Chrome('/home/shanmukh/Python-3.7.3/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.qool.com/');
driver.maximize_window()
time.sleep(2) # Let the user actually see something!
driver.save_screenshot('/home/shanmukh/Pictures/qool/main.png')

def save_screen(self):
    id0 = self.get_attribute('href')
    dummy_variable = id0[22:]
    print(dummy_variable)
    time.sleep(2)
    driver.save_screenshot('/home/shanmukh/Pictures/qool/%s.png'%dummy_variable)

id1 = driver.find_element_by_xpath('/html/body/header/div/a[1]')
id1.click()
save_screen(id1)

id2 = driver.find_element_by_xpath('/html/body/header/div/a[2]')
id2.click()
save_screen(id2)

id3 = driver.find_element_by_xpath('/html/body/header/div/a[3]')
id3.click()
save_screen(id3)

id4 = driver.find_element_by_xpath('/html/body/header/div/a[4]')
id4.click()
save_screen(id4)

id5 = driver.find_element_by_xpath('/html/body/header/div/a[5]')
id5.click()
save_screen(id5)

driver.quit()

