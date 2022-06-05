
import time
import logging
import csv
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = Options()  # Instantiate an options class for the selenium webdriver
chrome_options.add_argument("--incognito")

# chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.delete_all_cookies()




driver.implicitly_wait(10);
# From crunchbase get all the tags
url = "https://www.crunchbase.com/discover/organization.companies"
driver.get(url)







# get text blob

html_text = driver.page_source

#convert based on 'html parser'
soup = BeautifulSoup(html_text, 'html.parser')


print("BREAK\n")


# get main tags

button_tags = soup.find_all("div" );

# print(button_tags)


# x path works // means from all over , means any tag name with the attribute id with the value mat-input-23

# //*[@id="mat-input-32"]

# search_bar = driver.find_element(by="By.XPATH" , value="//*[@id='']")
# print(search_bar)
driver.implicitly_wait(10)
for i in range(100):

    try:
            XPATH_TUPLE = (By.XPATH , "/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[1]/div[1]/mat-accordion/mat-expansion-panel[1]/div/div/div[3]/advanced-filter/filter-identifier-no-suggestions/entity-grouped-by-parent-input/div/mat-form-field/div/div[1]/div[4]/input");
            abc = driver.find_element(*XPATH_TUPLE).send_keys("A")
            # driver.find_element(By.ID, "mat-input-32")
            # Find attribute by X-path

            #  Get source after clicking on the search bar

            print(driver.page_source.encode('utf-8'))


    except:
        driver.implicitly_wait(100)


# if you click on the search button , then only the overlay pops up .
# the path file for the overlay is only loaded once you click on the search bar

# class="cdk-overlay-container"
#
#
# class ="cdk-overlay-connected-position-bounding-box"
#
#
# id = "cdk-overlay-0"
#
# id="entity-grouped-by-parent-0"
#
#





# <button _ngcontent-client-app-c251="" mat-list-item="" role="treeitem" aria-level="1" class="mat-list-item mat-focus-indicator active-group ng-star-inserted" type="button" id="picker-item-a02d6141-a2f8-a33e-7131-4b13f355b206" aria-setsize="47" aria-posinset="1" aria-expanded="false" aria-owns="group-a02d6141-a2f8-a33e-7131-4b13f355b206"><span class="mat-list-item-content"><span mat-ripple="" class="mat-ripple mat-list-item-ripple"></span><span class="mat-list-text"></span><span _ngcontent-client-app-c251="" class="group-content"><entity-picker-group-label _ngcontent-client-app-c251="" _nghost-client-app-c249=""><span _ngcontent-client-app-c249="" class="label">Administrative Services (21)</span><span _ngcontent-client-app-c249="" class="dot"></span></entity-picker-group-label><icon _ngcontent-client-app-c251="" key="icon_caret_right"><svg viewBox="0 0 24 24" class="default accent"><path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"></path></svg></icon></span></span></button>

