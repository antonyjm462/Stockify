import webbrowser
from PIL import Image, ImageDraw
from selenium import webdriver
import webbrowser
import time
import os
from datetime import date
today = date.today()
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def browser():
    if(os.path.exists(BASE_DIR+"/dashboard/data/"+str(today)+".csv") != True):
        driver = webdriver.Chrome(executable_path=BASE_DIR+"/chromedriver_win32/chromedriver.exe")
        driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')
        button = driver.find_element_by_class_name('download-data-link1')
        button.click()
        time.sleep(5)
        driver.close()
        os.rename("C://Users//anton//Downloads//data.csv",BASE_DIR+"/dashboard/data/"+str(today)+".csv")

def main():
    browser()



if __name__ == "__main__":
    main()