from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_id("treasure")
	x_atr = x_element.get_attribute("valuex")
	y = calc(x_atr)

	input1 = browser.find_element_by_id("answer")
	input1.send_keys(y)

	input2 = browser.find_element_by_id("robotCheckbox")
	input2.click()

	input3 = browser.find_element_by_id("robotsRule")
	input3.click()
	
	button = browser.find_element_by_xpath('//button[text()="Submit"]')
	button.click()




	# input1 = browser.find_element_by_name("first_name")
	# input1.send_keys("Ivan")
	# input2 = browser.find_element_by_name("last_name")
	# input2.send_keys("Petrov")
	# input3 = browser.find_element_by_class_name("city")
	# input3.send_keys("Smolensk")
	# input4 = browser.find_element_by_id("country")
	# input4.send_keys("Russia")
	# button = browser.find_element_by_xpath('//button[text()="Submit"]')
	# button.click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()
	browser.close()
# не забываем оставить пустую строку в конце файла

