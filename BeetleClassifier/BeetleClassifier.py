# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:21:45 2020

@author: Christian
"""

import wavio
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

masterKey = {"bla":0,"ColRub":0,"Brsrub":0,"noise":0}
#########Creating the masterKey for Blatch
myPath = "blatch_files/" #where test data is stored
beetleType = "bla" #classification part of file name
normDataFFTavg = 0
for n in range(10):
    dataObj = wavio.read(myPath + beetleType + str(n+1) + ".wav") #reads data sample
    fs = dataObj.rate #sample rate
    data = dataObj.data[:,0] #audio is 2 channels, we are only interested in 1
    N = dataObj.data.shape[0] #length of signal
    sums = np.sum(np.absolute(data)) #normalizing the data for equivelant volume
    data = data/sums    
    fftData = np.fft.fft(data) #take fft of normalized data
    normDataFFTavg += fftData 
    
normDataFFTavg/=10 #average FFT data
sums = np.sum(np.absolute(normDataFFTavg)) #normalizing FFT data
normDataFFTavg = normDataFFTavg/sums
masterKey[beetleType] = np.absolute(normDataFFTavg) #place the master key for beetle type in dictionary
dummyx = np.linspace(0,fs,N) #plot master key data
dummyy = np.absolute(normDataFFTavg)
plt.subplot(221)
plt.title("Blatch")
plt.plot(dummyx,dummyy)
#########Creating the masterKey for Collaris
myPath = "collaris_files/"
beetleType = "ColRub"
normDataFFTavg = 0
for n in range(10):
    dataObj = wavio.read(myPath + beetleType + str(n+1) + ".wav")
    fs = dataObj.rate
    data = dataObj.data[:,0]
    N = dataObj.data.shape[0]
    sums = np.sum(np.absolute(data))
    data = data/sums
    fftData = np.fft.fft(data)
    normDataFFTavg += fftData
    
normDataFFTavg/=10
sums = np.sum(np.absolute(normDataFFTavg))
normDataFFTavg = normDataFFTavg/sums
masterKey[beetleType] = np.absolute(normDataFFTavg)
dummyx = np.linspace(0,fs,N)
dummyy = np.absolute(normDataFFTavg)
plt.subplot(222)
plt.title("Collaris")
plt.plot(dummyx,dummyy)
########Creating masterKey for Berosus
myPath = "berosus_files/"
beetleType = "Brsrub"
normDataFFTavg = 0
for n in range(10):
    dataObj = wavio.read(myPath + beetleType + str(n+1) + ".wav")
    fs = dataObj.rate
    data = dataObj.data[:,0]
    N = dataObj.data.shape[0]
    sums = np.sum(np.absolute(data))
    data = data/sums
    fftData = np.fft.fft(data)
    normDataFFTavg += fftData
    
normDataFFTavg/=10
sums = np.sum(np.absolute(normDataFFTavg))
normDataFFTavg = normDataFFTavg/sums
masterKey[beetleType] = np.absolute(normDataFFTavg)
dummyx = np.linspace(0,fs,N)
dummyy = np.absolute(normDataFFTavg)
plt.subplot(223)
plt.title("Berosus")
plt.plot(dummyx,dummyy)
########Creating masterKey for noise
myPath = "noise_files/"
beetleType = "noise"
normDataFFTavg = 0
for n in range(10):
    dataObj = wavio.read(myPath + beetleType + str(n+1) + ".wav")
    fs = dataObj.rate
    data = dataObj.data[:,0]
    N = dataObj.data.shape[0]
    sums = np.sum(np.absolute(data))
    data = data/sums
    fftData = np.fft.fft(data)
    normDataFFTavg += fftData
    
normDataFFTavg/=10
sums = np.sum(np.absolute(normDataFFTavg))
normDataFFTavg = normDataFFTavg/sums
masterKey[beetleType] = np.absolute(normDataFFTavg)
dummyx = np.linspace(0,fs,N)
dummyy = np.absolute(normDataFFTavg)
plt.subplot(224)
plt.title("Noise")
plt.plot(dummyx,dummyy)


##Reference sample against master key
sample = "beetleSamples/sample18.wav" #change this variable to the name of the test sample
dataObj = wavio.read(sample) #read sample
fs = dataObj.rate 
data = dataObj.data[:,0]
N = dataObj.data.shape[0]
sums = np.sum(np.absolute(data)) #normalize for volume
data = data/sums    
fftData = np.fft.fft(data) #normalize FFT
normDataFFTavg = np.power(np.absolute(fftData),0.2)
#normDataFFTavg = np.absolute(fftData)/sum(np.absolute(fftData))

ans = "" #name of classification
corr = 0 #best value
for key in masterKey.keys(): #correlate with all keys and check for similarity
    correlation = sum(np.multiply(normDataFFTavg,masterKey[key]))
    print(correlation)
    if correlation > corr:
        ans = key
        corr = correlation
        
print(ans + ": " + str(corr))