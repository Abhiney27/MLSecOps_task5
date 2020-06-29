ip = []
date= []
url = []

f = open('/root/MLSecOps/access_log.txt' , 'r')

for line in f:
    ip.append(line.split("- -")[0])
    date.append(line.split(']')[0].split('[')[1])
    url.append(line.split('"')[1].split('"')[0])

f.close()
        
        


import pandas as pd
from pandas import DataFrame


ip =  DataFrame(ip , columns=['ip'])
date =  DataFrame(date , columns=['date'])
url =  DataFrame(url , columns=['url'])
df = pd.concat([ip , date , url] , axis=1)

csv_data = df.to_csv(index=False)
df.to_csv('/root/MLSecOps/log.csv' , index=False)
pd.read_csv('/root/MLSecOps/log.csv')
