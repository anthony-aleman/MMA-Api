from selenium import webdriver
from bs4 import BeautifulSoup
import os
import pandas as pd


URL_ = 'http://www.ufcstats.com/statistics/fighters'

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver')
driver.implicitly_wait(3)

# load up url
driver.get(URL_)

# capture the fighter table
fighter_table = driver.find_elements_by_class_name('b-statistics__table-row')

jump_links = driver.find_elements_by_class_name('b-statistics__nav-item')

fighters = []
curr_link = 0
for i in range(65, 91):
    if jump_links[curr_link].text == chr(i):
        jump_links[curr_link].click()
        curr_link += 1
    count = 11
    all_ = driver.find_element_by_link_text('ALL')    
    all_.click()
    table_cols = driver.find_elements_by_class_name('b-statistics__table-col')
    while count < len(table_cols):
        fighter = []
        for j in range(0, 11):
            fighter.append(table_cols[count + j].text)
        fighters.append(fighter)
        count += 11
    jump_links = driver.find_elements_by_class_name('b-statistics__nav-item')

df = pd.DataFrame(fighters, columns=['FIRST', 'LAST', 'NICKNAME', 'HT', 'WT', 'REACH', 'STANCE', 'W', 'L', 'D', 'BELT'])

# TODO: transfer all of the data into a pandas dataframe, then transfer it into a csv file
df.to_csv('fighters.csv')