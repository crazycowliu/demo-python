#coding=utf-8 

from selenium import webdriver 


driver=webdriver.Firefox() 
driver.get("https://www.baidu.com") 

driver.set_window_size(800, 800)
driver.back()
#driver.find_element_by_id("kw").send_keys("Selenium2") 
#driver.find_element_by_id("su").click() 

'''
driver.find_element_by_xpath("//input[@id='kw']")

driver.find_element_by_css_selector("#kw") 
driver.find_element_by_css_selector(".s_ipt") 
driver.find_element_by_css_selector("map>area")
'''

# driver.quit()
