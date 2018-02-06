# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 07:37:23 2016

@author: haQQi
"""

import numpy as np 
#contoh fungsi
def PSa(z,m,r):
    if m>6.5:
		PGA = 10**(-1.274 + 1.1*m- 2.1 *np.log(r+(np.exp(-0.48451+0.524*m))))
    else:
		PGA = 10**(-0.642 + m- 2.1 *np.log(r+(np.exp(1.29649+0.25*m))))
    if PGA>z :    
        return 1. 
    else:
        return 0.

def psha(z,m,r,fmr,rate_of_occurence): 
    psha= 0.
    for i in range(len(m)):
        for j in range(len(r)):
            print j
            psha+=fmr[len(r)*j+i]*PSa(z,m[i],r[j])
    return rate_of_occurence*psha

#kasus 1
# z = 1 m/s^2
z=1. / 9.8
rate_of_occurence = 1.
fmr = [0.2,0.6,0.2]
m = [6.,7.,8.]
r = [13.]
psha1 = psha(z,m,r,fmr,rate_of_occurence)
print ('probabilitas gorund motion melebihi  %.4f dalam satu tahun adalah : %.4f\n'%(z,psha1))

#kasus 2
# z = 2 m/s^2
z=2. / 9.8
psha2 = psha(z,m,r,fmr,rate_of_occurence)
print ('probabilitas gorund motion melebihi  %.4f dalam satu tahun adalah : %.4f\n'%(z,psha2))  

#kasus 3
# z = 4 m/s^2
z=4. / 9.8
psha3 = psha(z,m,r,fmr,rate_of_occurence)
print ('probabilitas gorund motion melebihi  %.4f dalam satu tahun adalah : %.4f\n'%(z,psha3))     

