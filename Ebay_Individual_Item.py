import re
import time
import logging
import csv
from bs4 import BeautifulSoup
import itertools

from Ebay_Search_Bar import get_dictionary_ebay
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def get_individual_item(link):


    chrome_options = Options()  # Instantiate an options class for the selenium webdriver
    chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    empty = " "
    driver.implicitly_wait(10)


    try:

        #url = "https://www.ebay.com/itm/264461773926?epid=62894632&hash=item3d93266c66:g:Nx8AAOSw31RgUEZm&amdata=enc%3AAQAHAAAA0AlTQWq3z20Qnla%2B4B40NU%2FfqZpwKFmcoIDgw3AKMgCByWb7d%2FN5zY82E2iFQT4gkA60AaMyE1npuOA5NmCvJGi%2F5l9esMtJSlJ8QPqvp5f2meBEaHSBBojMc4Z6jrwiHu608HBubkgwr9aTP6IjKcDl1xL4cVszttEmijlv%2BP%2BesfWdUxO2OMBuS87H%2FwMZmdNEO0QMMsdD04kzQl1xHTqbQxvCX3HtOTakoOlLFJgYtOjK%2BKuqPaKDnYmboRXNMiN1iEllY0xPHy0qjl4cqsc%3D%7Ctkp%3ABFBMyqvG3KZg"
        driver.get(link)
        time.sleep(10)

        html_text = driver.page_source
        #convert based on 'html parser'
        soup = BeautifulSoup(html_text, 'html.parser')

        div_container = soup.find("div" , {"class" : "mainPrice"})
        price = div_container.find("span" , {"itemprop" : "price"})
        # print(price.get_text())
        return price.get_text()
    except:
        return NULL;


