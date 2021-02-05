from selenium import webdriver
from time import sleep
from threading import *
driver1=webdriver.Chrome(executable_path=r'C:/Users/vishal/Downloads/chromedriver_win32/chromedriver.exe')
driver2=webdriver.Chrome(executable_path=r'C:/Users/vishal/Downloads/chromedriver_win32/chromedriver.exe')
driver3=webdriver.Chrome(executable_path=r'C:/Users/vishal/Downloads/chromedriver_win32/chromedriver.exe')
driver4=webdriver.Chrome(executable_path=r'C:/Users/vishal/Downloads/chromedriver_win32/chromedriver.exe')
class one(Thread):
    def run(self):
        n=20
        driver1.get("https://www.youtube.com/watch?v=E-9Ff1yJ478")
        while(n):
             n=n-1
             sleep(10)
             driver1.refresh()



class two(Thread):
    def run(self):
        n=20
        driver2.get("https://www.youtube.com/watch?v=E-9Ff1yJ478")
        while(n):
             n=n-1
             sleep(10)
             driver2.refresh()



class three(Thread):
    def run(self):
        n=20
        driver3.get("https://www.youtube.com/watch?v=E-9Ff1yJ478")
        while(n):
             n=n-1
             sleep(10)
             driver3.refresh()



class four(Thread):
    def run(self):
        n=20
        driver4.get("https://www.youtube.com/watch?v=E-9Ff1yJ478")
        while(n):
             n=n-1
             sleep(10)
             driver4.refresh()
    






t1=one()
t2=two()
t3=three()
t4=four()
t1.start()
t2.start()
t3.start()
t4.start()
