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
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def browser():
    download = get_download_path()
    if(os.path.exists(BASE_DIR+"/dashboard/data/"+str(today)+".csv") != True):
        driver = webdriver.Chrome(executable_path=BASE_DIR+"/chromedriver_win32/chromedriver.exe")
        driver.get('https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')
        button = driver.find_element_by_class_name('download-data-link1')
        button.click()
        time.sleep(5)
        driver.close()
        print(get_download_path())
        os.rename(download+"\data.csv",BASE_DIR+"/dashboard/data/"+str(today)+".csv")

def main():
    browser()




if __name__ == "__main__":
    main()