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


count = 1

with open('data.csv') as csv_file:
    try:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            # print (row)

            url = row[0]
            url = url.replace('﻿https:', 'https:')

            driver.get(url)


            html31 = driver.page_source
            html36 = BeautifulSoup(html31, "lxml", from_encoding="utf-8")


            brand = ''
            desc = ''
            description =''

            try:
                brand_a = html36.find('a',{'id':'bylineInfo'})
                brand_a = brand_a.text.strip()

                if 'Brand' in brand_a:
                    brand = brand_a
                    brand = brand.replace('Brand','')
                    brand = brand.replace(':', '')

            except:
                print ("eror")



            if brand == '':
                try:
                    table_brand = html36.find('table',{'id':'productDetails_detailBullets_sections1'})

                    # print (table_brand)

                    trs = table_brand.find_all('tr')

                    for tr in trs:
                        tr_data = tr.text.strip()
                        # print (tr_data)

                        if 'Manufacturer' in tr_data:
                            brand = tr_data
                            brand = brand.replace('Manufacturer','')
                            brand = brand.replace('\n','')



                except:
                    print ("eror")









            try:
                desc = html36.find('div', {'id': 'featurebullets_feature_div'})
                desc = desc.text.strip()
                text = os.linesep.join([s for s in desc.splitlines() if s])

                text = text.replace('About this item\n', '')
                text = text.replace('This fits your .\n', '')
                text = text.replace('Make sure this fits\n', '')
                text = text.replace('by entering your model number.\n', '')

                desc = text
                # print (desc)




            except:
                print ("Error")


            text = ''


            try:
                descriptionhtml = html36.find('div',{'id':'productDescription'})

                descriptionhtml = descriptionhtml.find_all('p')

                for des in descriptionhtml:
                    description = description + des.text.strip() + '\n'


            except:
                print ('rtt')


            row.append(brand)
            row.append(desc)
            row.append(description)

            arr = []

            arr.append(row)
            print (row)
            with open('1_1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(arr)

    except:
        print ("errors")




