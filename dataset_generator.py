ip = []
date= []
url = []
f = open('access_log' , 'r')
for line in f:
    ip.append(line.split("- -")[0])
    date.append(line.split(']')[0].split('[')[1])
    url.append(line.split('"')[1].split('"')[0])
        
        


import pandas as pd
from pandas import DataFrame


ip =  DataFrame(ip , columns=['ip'])
date =  DataFrame(date , columns=['date'])
url = df =  DataFrame(url , columns=['url'])
dataset = pd.concat([ip , date , url] , axis=1)

csv_data = dataset.to_csv(index=False)
dataset.to_csv('log.csv' , index=False)