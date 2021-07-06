import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import csv
import os
import xlsxwriter



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

with open('brand.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        temp = row

        print (temp)
        url = temp[0]
        url = url.replace('﻿https:', 'https:')

        driver.get(url)

        html31 = driver.page_source
        html36 = BeautifulSoup(html31, "lxml", from_encoding="utf-8")

        brand = ''

        if brand == '':
            try:
                table_brand = html36.find_all('table')

                for table in table_brand:

                    if brand != '':
                        break

                    trs = table.find_all('tr')


                    for tr in trs:
                        tr_data = tr.text.strip()
                        print (tr_data)

                        if 'Brand' in tr_data:
                            if brand == '':
                                brand = tr_data
                                brand = brand.replace('Brand', '')
                                brand = brand.replace('\n', '')
                                break

                            else:
                                break

                        if 'Manufacturer' in tr_data:
                            if brand == '':
                                brand = tr_data
                                brand = brand.replace('Manufacturer', '')
                                brand = brand.replace('\n', '')
                                break

                            else:
                                break



            except:
                print ("eror")


        print (brand)

        temp[4] = brand

        arr =[]

        arr.append(temp)

        with open('brand_empty_1.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(arr)

driver.close()