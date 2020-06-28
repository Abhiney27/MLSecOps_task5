import pandas as pd
import numpy as np
df = pd.read_csv('log.csv')
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.preprocessing import StandardScaler
X =  df.iloc[: , :]
X = X.to_numpy()

label = LabelEncoder()
ip = label.fit_transform(X[:,0])
date = label.fit_transform(X[:,1])
url = label.fit_transform(X[:,2])

IP  = pd.DataFrame(ip , columns=["IP"])
DATE  = pd.DataFrame(date , columns=["DATE"])
URL  = pd.DataFrame(url , columns=["URL"])

dataset = pd.concat([IP , DATE , URL] , axis=1)
src = StandardScaler()
data_scaled = src.fit_transform(dataset)

from sklearn.cluster import KMeans
model = KMeans()
model.fit(data_scaled)
pred  =  model.fit_predict(data_scaled)
data_scaled = pd.DataFrame(data_scaled  ,columns=['IPs'  ,'DATE' , 'URL'])
data_scaled['cluster name'] = pred

IPs_result = pd.concat([df['ip'] , dataset['IP']] , axis=1)


def CountFrequency(ip_list , ip_label):
    
    
    freq = {}
    for item in ip_list:
        if(item in freq):
            freq[item] +=1
        else:
            freq[item] = 1
    
    max_freq = 0
    max_key = 0
    for key , value in freq.items():
        
        if value > max_freq:
        
            max_freq = value                    
            max_key = key
            
    return ip_label[ip_list.index(max_key)]

ip_res = CountFrequency(IPs_result['IP'].tolist(), IPs_result['ip'].tolist())


file1 = open("blocked_ip.txt","w")
file1.write(ip_res)
file1.close()
                