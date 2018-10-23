from selenium import webdriver
import time


br = webdriver.Firefox(executable_path= 'C:/Users/Student/Desktop/Pycharm/geckodriver.exe')
br.implicitly_wait(15)
br.get('http://www.omdbapi.com/')
search = br.find_element_by_name('q')
search.send_keys('blade runner')
search.submit()
time.sleep(5)
print(br.title)
