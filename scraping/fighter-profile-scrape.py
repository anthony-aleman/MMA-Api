from selenium import webdriver
import pandas as pd


URL_ = 'http://www.ufcstats.com/statistics/fighters'

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver')
driver.implicitly_wait(3)

#driver.get(URL_)


fighter_links = driver.find_elements_by_class_name('b-link b-link_style_black')
jump_links = driver.find_elements_by_class_name('b-statistics__nav-item')
table_cols = driver.find_elements_by_class_name('b-statistics__table-col')
curr_link = 0
df = pd.read_csv('./scraping/fighters.csv')
print(df.columns)




for i in range(65, 91):
    if jump_links[curr_link].text == chr(i):
        jump_links[curr_link].click()
        curr_link += 1
    count = 11
    all_ = driver.find_element_by_link_text('ALL')    
    all_.click()
    fighter_links = driver.find_elements_by_class_name('b-link b-link_style_black')
    while count < len(fighter_links):
        # find the link for the fighter
        link = table_cols[count]
        # click
        link.click()
        print(link)
        count += 11
    jump_links = driver.find_elements_by_class_name('b-statistics__nav-item')

