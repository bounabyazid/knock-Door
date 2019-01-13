#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:40:16 2019

@author: Yazid, Kein, Sari
"""

#https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error

#https://www.instructables.com/id/ESP32-With-ESP-Now-Protocol/

#use i2C ESP32



from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

import test
from fuzzywuzzy import fuzz

import acoustid
import chromaprint

def plot_wav(filename):
    rate,data = wavfile.read(filename)
    times = np.arange(len(data))/float(rate)

    # You can tweak the figsize (width, height) in inches
    plt.figure(figsize=(30, 4))
    plt.fill_between(times, data[:,0], data[:,1], color='k') 
    plt.xlim(times[0], times[-1])
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    # You can set the format by changing the extension
    # like .pdf, .svg, .eps
    plt.savefig(filename+'.png', dpi=100)
    plt.show()

def FingerPrintAudio(filename):   
    duration, fp_encoded = acoustid.fingerprint_file(filename)
    fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)
    #print(fingerprint)
    return fingerprint

def Correlation():
    i=1
    
def AudioSimilarity(sample_fingerprint, fingerprint):
    similarity = fuzz.ratio(sample_fingerprint, fingerprint)
    #print(similarity)
    return similarity

FP1 = FingerPrintAudio("yazi1.wav")
FP2 = FingerPrintAudio("yazi2.wav")

simlarity = AudioSimilarity(FP1, FP2)

if simlarity >= 95:
   test
   print ('Doore Opening')

else:
   print ('Fuck off')


#plot_wav("yazi1.wav")
#plot_wav("yazi2.wav")
