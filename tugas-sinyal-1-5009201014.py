#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter

def myFFT(v):
    n = len(v)
    
    if n==1:
        return v
    else:
        # implement some recursive
        F_even = myFFT(v[::2])
        F_odd = myFFT(v[1::2])
        
        # frequency factor
        fac = np.exp(-2j*np.pi*np.arange(n)/n)
        
        # build FFT array
        F = np.concatenate([
            F_even + fac[:int(n/2)]*F_odd,
            F_even + fac[int(n/2):]*F_odd
            ])
        
        return F

# ID
print("Nama: Ijlal Abdus Salam")
print("NRP: 5009201014")

# X array linear spacing
x = np.arange(0, 2, 1.0/64)
X = np.sin(2*np.pi*x)


# Y sinus function
Y = np.cos(2*np.pi*x)

# create noise array at X length
R = np.arange(0, 1, 1.0/128)

# add noise to sine result
Yr = Y + R + X 

# FFT all
FY = np.abs(myFFT(Y))
FYr = np.abs(myFFT(Yr))

#filter 
window_length = 15  
polyorder = 2  
Yr_savgol = savgol_filter(Yr, window_length, polyorder)

sigma = 2  
Yr_gaussian = gaussian_filter(Yr, sigma)

# plot all
fig, ax = plt.subplots(3,2)
ax[0,0].plot(X,Y)
ax[0,1].plot(FY)
ax[1,0].plot(X,Yr)
ax[1,1].plot(FYr)
ax[2,0].plot(Yr_savgol)
ax[2,1].plot(Yr_gaussian)


# In[ ]:




