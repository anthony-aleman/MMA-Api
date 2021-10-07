from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

URL_ = 'http://www.ufcstats.com/statistics/fighters'

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver')
driver.implicitly_wait(3)

# load up url
driver.get(URL_)

# capture the fighter table
fighter_table = driver.find_elements_by_class_name('b-statistics__table-row')


for fighter in fighter_table:
    # TODO: use regex to capture the 11 groups of fighter information
    # using the split method only sort of works at will seperate the height feet and height inches as well as the weight.
    print(fighter.text.split())

# TODO: transfer all of the data into a pandas dataframe, then transfer it into a csv file
