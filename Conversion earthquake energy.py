

import csv       
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np




#konversi magnitudo
time = []
mag = []
energi = []
with open ("gempantt.csv") as data:
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        time.append(row[0])
        if row[5] == 'mb':
            value = 10**(5.8 + (2.4*(float(row[4]))))
            mag.append(float(row[4]))
            energi.append(value)
        elif row[5] == 'ms':
            mb = float((8.545 + float(row[4]))/1.201)
            value = float(10**(5.8 + (2.4*(float(row[4])))))
            mag.append(float(row[4]))
            energi.append(value)
        elif row[5] == 'mw' or 'mwc' or 'mwb' or 'ml':
            value = float(10**(11.8+(1.5*float(row[4]))))
            mag.append(float(row[4]))
            energi.append(value)
            
#konversi waktu
date = []
for i in time:
    a = datetime.strptime(i, '%Y-%m-%dT%H:%M:%S.%fZ')
    date.append(a)

days = []
for i in date:
    a = i - date[4251]
    days.append(a.days)
    
lst= list()
D = days
T = (1.0/800.0)
t = 2
wt = ((2*np.pi)/T)*t

for i in D:
    y = ((3*np.sin(wt*(i)))+(np.cos(wt*(i)+0.35*np.pi)))
    lst.append(y)
    
    
energis= list()
D = energi
T = (1.0/800.0)
t = 2
wt = ((2*np.pi)/T)*t

for i in D:
    y = ((3*np.sin(wt*(i)))+(np.cos(wt*(i)+0.35*np.pi)))
    energis.append(y)    

    



plt.plot(energis,lst)
plt.title('Grafik TimeSeries \n Frequency vs magnitudo')
plt.ylabel('Energi')
plt.xlabel('Hz')
#plt.savefig('timeenergi.jpg',dpi=400)
plt.show()
