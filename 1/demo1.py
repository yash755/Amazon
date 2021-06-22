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


# count = 1
#
#
# workbook = xlsxwriter.Workbook('demo_file_786.xlsx')
# worksheet = workbook.add_worksheet()
# line_count = 0


with open('amazon52.csv') as csv_file:
    try:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            print (row)

            url = row[0]
            url = url.replace('﻿https:', 'https:')

            driver.get(url)


            html31 = driver.page_source
            html36 = BeautifulSoup(html31, "lxml", from_encoding="utf-8")

            try:
                desc = html36.find('div', {'id': 'featurebullets_feature_div'})
                desc = desc.text.strip()
                text = os.linesep.join([s for s in desc.splitlines() if s])

                text = text.replace('About this item\n', '')
                text = text.replace('This fits your .\n', '')
                text = text.replace('Make sure this fits\n', '')
                text = text.replace('by entering your model number.\n', '')

                desc = text
                print (desc)

                row.append(desc)


            except:
                print ("Error")


            text = ''


            try:
                description = html36.find('div',{'id':'productDescription'})

                description_p = description.find('p')

                # if description.text.strip() != '':
                text = os.linesep.join([s for s in description_p.text.strip().splitlines() if s])
                print (text)
                row.append(text)



            except:
                print ('rtt')


            # if text == '':
            #
            #     try:
            #         description_1 = html36.find('div', {'id': 'prodDetails'})
            #
            #         if description_1.text.strip() != '':
            #             text = os.linesep.join([s for s in description_1.text.strip().splitlines() if s])
            #             row.append(text)
            #
            #
            #
            #     except:
            #         print ('rtt')





            arr = []

            arr.append(row)
            print (arr)
            with open('sydney4.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(arr)

    except:
        print ("errors")


driver.close()