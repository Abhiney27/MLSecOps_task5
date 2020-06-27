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
url =  DataFrame(url , columns=['url'])
df = pd.concat([ip , date , url] , axis=1)

csv_data = df.to_csv(index=False)
df.to_csv('log.csv' , index=False)
