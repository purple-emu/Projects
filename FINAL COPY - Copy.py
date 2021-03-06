import bs4, requests, os, time, openpyxl
from selenium import webdriver

##Open Excel

DIR = os.getcwd()
os.chdir(DIR)
wb = openpyxl.load_workbook('2. Final Project - Team 7 - Financial Analytics.xlsm',read_only =False, keep_vba=True)
ws = wb["Raw Data"]

##METRO

def Metro_getprice():

    driver = webdriver.Chrome()

    MetroURL = []

    for i in range (0,22):
        MetroURL.append(ws['E' + str(i+2)].value)

    print (MetroURL)

    MetroPrice = []

    def metro (url):
        driver.get(url)
        time.sleep(5)
        element = driver.find_element_by_class_name("pi-price.price-update")
        return element.text

    for i in range (0,22):
        MetroPrice.append(metro(MetroURL[i]))

    print (MetroPrice)

    for i in range (0,22):
        ws['F' + str(i+2)] = MetroPrice[i]

    driver.quit()

##Walmart
    
def WalMart_getprice():

    driver = webdriver.Chrome()

    WalURL = []

    for i in range (0,22):
        WalURL.append(ws['G' + str(i+2)].value)

    print (WalURL)

    WalPrice = []

    def wal (url):
        driver.get(url)
        time.sleep(5)
        element = driver.find_element_by_class_name("css-rykmet.esdkp3p2")
        return element.text

    for i in range (0,22):
        WalPrice.append(wal(WalURL[i]))

    print (WalPrice)

    for i in range (0,22):
        ws['H' + str(i+2)] = WalPrice[i]

    driver.quit()

##Loblaws
    
def Loblaws_getprice():
        driver = webdriver.Chrome()

        LobURL = []

        for i in range (0,22):
            LobURL.append(ws['I' + str(i+2)].value)

        print (LobURL)

        LobPrice = []

        def lob (url):
            driver.get(url)
            time.sleep(5)
            element = driver.find_element_by_class_name("price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value")
            return element.text

        for i in range (0,22):
            LobPrice.append(lob(LobURL[i]))

        print (LobPrice)

        for i in range (0,22):
            ws['J' + str(i+2)] = LobPrice[i]

        driver.quit()

##ValuMart

def ValuMart_getprice():
    driver = webdriver.Chrome()

    ValURL = []

    for i in range (0,22):
        ValURL.append(ws['K' + str(i+2)].value)

    print (ValURL)

    ValPrice = []

    def val (url):
        driver.get(url)
        time.sleep(5)
        element = driver.find_element_by_class_name("price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value")
        return element.text

    for i in range (0,22):
        ValPrice.append(val(ValURL[i]))

    print (ValPrice)

    for i in range (0,22):
        ws['L' + str(i+2)] = ValPrice[i]

    driver.quit()

##Superstore
    
def SuperStore_getprice():
    driver = webdriver.Chrome()

    SupURL = []

    for i in range (0,22):
        SupURL.append(ws['M' + str(i+2)].value)

    print (SupURL)

    SupPrice = []

    def sup (url):
        driver.get(url)
        time.sleep(5)
        element = driver.find_element_by_class_name("price__value.selling-price-list__item__price.selling-price-list__item__price--now-price__value")
        return element.text

    for i in range (0,22):
        SupPrice.append(sup(SupURL[i]))

    print (SupPrice)

    for i in range (0,22):
        ws['N' + str(i+2)] = SupPrice[i]

    driver.quit()

##Run
    
import threading
if __name__ == '__main__':
    p1 = threading.Thread(target = Metro_getprice)
    p2 = threading.Thread(target = WalMart_getprice)
    p3 = threading.Thread(target = Loblaws_getprice)
    p4 = threading.Thread(target = ValuMart_getprice)
    p5 = threading.Thread(target = SuperStore_getprice)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

##Save Excel

from datetime import datetime

ws ['B25'] = "Last updated:"
ws ['C25'] = datetime.now()

wb.save('2. Final Project - Team 7 - Financial Analytics - Updated.xlsm')
