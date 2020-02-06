# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:11:38 2019

@author: igloo
"""

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the csv file storing stock symbol list
with open('./zacks_custom_screen_2019-09-12.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    articles = []
    for row in readCSV:
        symbol = row[1]
        # Access the web for selected symbol
        driver.get("https://finance.yahoo.com/quote/"+symbol+"/history?p="+symbol)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/span[2]/span/input").click()
        time.sleep(2)
        element = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/span[2]/div/input[1]")
        
        # Specify time period as max
        period = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/span[2]/div/div[1]/span[8]");
        period.click();
        driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/span[2]/div/div[3]/button[1]").click()
        time.sleep(1)

        # Specify show as dividends only
        show = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[2]/span/div/span");
        show.click();
        wait = WebDriverWait(driver, 10)
        split = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[2]/span/div[2]/div[3]/span")))
        split.click()

        # Specify frequency as monthly
        frequency = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[3]/span/div/span")
        frequency.click()
        wait = WebDriverWait(driver, 10)
        tp1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[3]/span/div[2]/div[3]/span")))
        tp1.click();
        time.sleep(2)

        # Click apply button
        button = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/button")
        time.sleep(3)
        button.click()
        
        # Download displayed data
        download = driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[2]/span[2]/a/span")
        download.click()
        
        time.sleep(10)
 
    driver.close()


