#coding=utf-8 
import binascii
import os
import time
from selenium import webdriver
from Crypto.Cipher import AES
from asyncio.tasks import sleep

def read_key(): 
    file_object = open('.\\input.\\key', 'r')
    try:
        encrpted = file_object.read()
        #print(encrpted)
        byte_arr = bytearray.fromhex(encrpted)
        #print(byte_arr)
        
        key = b'abcdefgh        ' 
        aes = AES.new(key, AES.MODE_ECB) 
        byte_arr = aes.decrypt(byte_arr)
        #print(byte_arr)
        hex_str = binascii.b2a_hex(byte_arr)
        #print(hex_str)
        
        s = str(byte_arr,encoding='utf-8',errors="ignore")
        #print(s)
        #print(s[:10])
        return s[:10]
    finally:
        file_object.close()

env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}

print (env_dist.get('JAVA_HOME'))
print (env_dist['JAVA_HOME'])

# 打印所有环境变量，遍历字典
for key in env_dist:
    print (key + ' : ' + env_dist[key])

    
driver = webdriver.Firefox() 

#driver.get("https://www.aex-global.com/") 
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/a[1]").click()

# login page

driver.get("https://www.aex-global.com/page/register.html?type=2") 

driver.find_element_by_xpath("//*[@id='my_self_email']").send_keys("4282198@qq.com") 

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/ul/li[2]/div/input").send_keys(read_key()) 

driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/ul/a").click()

time.sleep(5)

driver.get("https://www.aex-global.com/page/gat_description.html?type=get") 

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[5]/a").click()

# "Get GAT" -> /html/body/div[2]/div[2]/div/div[2]/div/div/div/ul/li[2]/a
# "Get GAT" -> https://www.aex-global.com/page/gat_description.html?type=get

#driver.find_element_by_id("html body div[2]/div[2]/div/div[3]/a[1]")

# driver.quit()
