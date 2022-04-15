import pandas as pd
from datetime import datetime
from selenium import webdriver
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get('https://www.worldometers.info/coronavirus/')
table = driver.find_element_by_id('main_table_countries_today')
ls = table.find_elements_by_xpath(".//tr")
df=pd.DataFrame([[(j.text.replace(',','').replace('+','') if j.text!="" else 0) for j in i.find_elements_by_xpath(".//td")][1:-1] for i in ls if i.text!=""][1:-1],columns = ['Country', 'Total Cases', 'New Cases','Total Deaths','New Deaths','Total Recovered','New Recovered','Active Cases','Serious','Tot per 1M','Deaths per 1M','Tests','Tests per 1M','Pop'])
df.to_csv('data/'+str(datetime.date(datetime.now()))+'.csv')
driver.quit()
