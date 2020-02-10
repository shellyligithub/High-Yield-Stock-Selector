# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:46:10 2019

@author: igloo
"""

import csv
from pretty_print import pretty_print3 ## print out formatting

# Stock data was stored in separate csv file by running collectDividendHistory.py
# Assume they are stored at ./stockDB/dividen/symbol.csv

print('How many years of historical stock dividend data you would like to analyze?\n')
yearToAnalyze= input('Enter the number for years:')
print('your like to compare ' + yearToAnalyze + ' years of dividend data\n')

targetGrowthRate= input('What is your target of growth rate? Ex: 2 for 200% \n')
print('your criteria for growth rate is ' + targetGrowth

map = {}
with open('./zacks_custom_screen_2019-09-12.csv') as stockList:
    readList = csv.reader(stockList, delimiter=',')
    for item in readList:
        symbol = item[1]
        dict = {}
        with open('./stockDB/dividend/'+symbol+'.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if(row[0] == 'Date'): 
                    continue
                date = row[0].split('-')
                dividend = float(row[1])
                yearMonth = date[0]+date[1]
                # Store dividend data hash table based on the distribution month and year as key
                dict[yearMonth] = {'dividend':dividend}
                
                # Round up distribution date to the following month 
                if(date[1] == '12'):
                    date[1] = '01'
                    date[0] = str(int(date[0])+1)
                else:
                    date[1] = str(int(date[1])+1)
                    if(len(date[1]) == 1):
                        date[1] = '0' + date[1]
        
                # Open stock historical price data
                with open('./stockDB/price/'+symbol+'.csv') as csvfile2:
                    readCSV2 = csv.reader(csvfile2, delimiter=',')
                    for row2 in readCSV2:
                        # Skip header row
                        if(row2[0] == 'Date'): 
                            continue
                        date2 = row2[0].split('-')
                        # Store stock price data hash table based on the distribution month and year as key
                        if(date[0]+date[1] == date2[0]+date2[1]):
                            dict[yearMonth]['price'] = float(row2[1])
        
        # Dump hash table into 2D array
        c, r = 5, len(dict);
        array = []
        for i in range(r):
            array.append([1]*c)
            
        i = 0
        for x in sorted(dict.keys()):
            j = 0
            array[i][j] = x
            for y in dict[x].keys():
                j = j + 1
                array[i][j] = dict[x][y]
            i = i + 1
        
        
        for i in range(len(dict)):
            array[i][4] = array[i][1]*array[i][3]
            if(i+1 < len(dict)):
                array[i+1][3] = array[i][3] + array[i][4]/array[i][2]
            print(array[i])
            print
    
        # user specified years of gain
        cur = array[len(array)-1]
        print(cur)
        if(cur[0] == '201909'):
            cur = array[len(array)-2]
        curYear = cur[0][0:4]
        curMonth = cur[0][4:]
        previousYearBack = str(int(curYear)-int(yearToAnalyze))
        prv = cur
        for i in range(len(array)):
            if(array[i][0] == previousYearBack + curMonth):
                prv = array[i]
                print(prv)
                gain = cur[3]/prv[3]*cur[2]/prv[2]
                print(symbol,gain)
                map[symbol] = gain

for k in map.keys(): 
    if(map[k] >= int(targetGrowthRate)):
        pretty_print3(k, map[k])
csv_or_not = input('Enter y to export to csv file，Enter other to exit：')

# Generated stock list with growth rate (gain)
if csv_or_not == 'y':
    csv = open('./stockFilterResult.csv', 'w+', encoding='utf-8')
    csv.write('Symbol,Gain,\n')
    for k in map.keys():
        csv.write(k + ',' + str(map[k]) + ',\n')
    csv.close()
    print('csv file has been saved in your folder')
else:
    quit()        

        
        
