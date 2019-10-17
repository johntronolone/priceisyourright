import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

from operator import truediv 

def sort_list(list1, list2): 
  
    zipped_pairs = zip(list2, list1) 
  
    z = [x for _, x in sorted(zipped_pairs)] 
      
    return z 


colsToExtract = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14]

# 0 PROCEDURE_CODE
# 1	PROCEDURE_NAME
# 2 SHORT_DESCRIPTION
# 3 CATEGORY_NAME
# 4 COVERAGE_CLASS
# 5 MED_ALLOW
# 6 PRICE_PERCISION
# 7 PATIENT_COMPLEXITY
# 8 PAYER
# 9 PLAN_TYPE
# 10 PROVIDER_NAME
# 11 ADDRESS1
# 12 CITY1
# 13 STATE1
# 14 ZIP1

data = pd.read_csv('NHID_csv.csv',
	header=0,
	usecols=colsToExtract,
	dtype = {14: 'str'})


categories = ['CATEGORY_NAME', 'PAYER', 'PLAN_TYPE', 'STATE1']
titles = ['Avg. Operation Cost per Service', 'Avg. Operation Cost per Provider', 'Avg. Operation Cost per Type', 'Avg. Operation Cost per State']

fig, axes = plt.subplots(1, len(categories))
fig.suptitle('NHID Exploratory Data Analysis')

formatter = ticker.FormatStrFormatter('$%1.2f')

for j in range(len(categories)):

	# clear arrays to store information as it's extracted from each row
	nameList = []
	countList = []
	sumList = []

	for i in range(len(data)):

		if not data[categories[j]][i].upper() in nameList:
			nameList.append(data[categories[j]][i].upper())
			countList.append(1)
			sumList.append(int(data[' MED_ALLOW '][i].replace('$','').replace(',','')))
		else:
			listIdx = nameList.index(data[categories[j]][i].upper())	
			countList[listIdx] = countList[listIdx] + 1
			sumList[listIdx] = sumList[listIdx] + int(data[' MED_ALLOW '][i].replace('$','').replace(',',''))

	avgList = list(map(truediv, sumList, countList))

	avgList, nameList = zip(*sorted(zip(avgList, nameList)))

	axes[j].bar(x=list(nameList), height=list(avgList))
	axes[j].set_title(str(titles[j]) + '\n(MED_ALLOW vs. ' + str(categories[j]) + ')')
	axes[j].tick_params(axis='x', labelrotation=90)

	axes[j].yaxis.set_major_formatter(formatter)

plt.show()


# todo: add a heat map

