from __future__ import division
import numpy as np
import math
import json
import collections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

published2016 = np.array([0.102, 0.0893, 0.159, 0.183, 0.233, 0.290, 0.350, 0.436, 0.505, 0.607, 0.705, 0.796, 0.931, 1.03, 1.07, 1.19, 1.27, 1.38, 1.49, 1.59, 1.64, 1.74, 1.83, 1.86, 1.89, 1.96, 2.02, 2.02, 2.00, 1.99, 1.99, 2.02, 1.99, 2.02,  2.02, 2.02, 1.92, 2.00, 1.98, 1.92, 1.88, 1.86, 1.91, 1.91, 1.94, 1.84, 1.77, 1.84, 1.94, 1.80, 1.75, 1.72, 1.77, 1.74, 1.86, 2.20, 1.43])*10**(-4)
published2016binnings = np.array([1, 1.16, 1.33, 1.51, 1.71, 1.92, 2.15, 2.4, 2.67, 2.97, 3.29, 3.64, 4.02, 4.43, 4.88, 5.37, 5.9, 6.47, 7.09, 7.76, 8.48, 9.26, 10.1, 11, 12, 13, 14.1, 15.3, 16.6, 18, 19.5, 21.1, 22.8, 24.7, 26.7, 28.8, 31.1, 33.5, 36.1, 38.9, 41.9, 45.1, 48.5, 52.2, 56.1, 60.3, 64.8, 69.7, 74.9, 80.5, 93, 108, 125, 147, 175, 211, 259, 450])
publishederrorbar = np.array([0.031, 0.0175, 0.02, 0.018, 0.022, 0.024, 0.028, 0.031, 0.035, 0.04, 0.044, 0.047, 0.058, 0.06, 0.06, 0.07, 0.07, 0.07, 0.07, 0.08, 0.08, 0.07, 0.08, 0.08, 0.09, 0.09, 0.09, 0.09, 0.09, 0.08, 0.08, 0.08, 0.08, 0.07, 0.07, 0.07, 0.06, 0.08, 0.08, 0.09, 0.09, 0.1, 0.1, 0.11, 0.11, 0.12, 0.13, 0.14, 0.15, 0.13, 0.15, 0.18, 0.2, 0.27, 0.41, 0.56, 0.53])*10**(-4)
'''
NNbinnings = np.array([16.6, 18.0, 19.5, 21.1, 22.8, 24.7,26.7,28.8,31.1,33.5,36.1,38.9, 41.9, 45.1, 48.5, 52.2, 56.1, 60.3, 64.8, 69.7, 74.9, 80.5, 93, 108, 125, 147, 175, 211, 250, 330, 525])
NN = np.array([0.00030,0.00030,0.00030,0.00030,0.00030,0.00030,0.00030,0.00030,0.00030,0.00030,0.000191,0.000178,0.00030,0.000180,0.000185,0.000182,0.000169,0.000177,0.000166,0.000184,0.000170,0.000169,0.000178,0.000149,0.000145,0.000203,0.000173,0.000245,0.000242,0.000300])
'''
NNbinnings = np.array([36.1,38.9, 41.9, 45.1, 48.5, 52.2, 56.1, 60.3, 64.8, 69.7, 74.9, 80.5, 93, 108, 125, 147, 175, 211, 250, 330, 525])
NN = np.array([0.000191,0.000178,0.000180,0.000180,0.000185,0.000182,0.000169,0.000177,0.000166,0.000184,0.000170,0.0001704,0.0001762,0.0001513,0.0001502,0.0002097,0.0001799,0.0002482,0.0002500,0.0002500])
########################## 41-45 should be empty ######################################

NNpoint=np.array( np.zeros(NNbinnings.shape[0]-1) )
int=np.array( np.zeros(NNbinnings.shape[0]-1) )
for i in range(NNpoint.shape[0]):
    NNpoint[i]=(NNbinnings[i]+NNbinnings[i+1])/2
published2016point=np.array( np.zeros(published2016binnings.shape[0]-1) )
for i in range(published2016point.shape[0]):
    published2016point[i]=(published2016binnings[i]+published2016binnings[i+1])/2

######################################### ratio and chi2  ##################################################################################################
plt.figure(figsize=(18,9))
plt.xlim(0,550)
#plt.ylim(0, max(NN)*1.5)
plt.plot(NNpoint, NN , 'gs',lw=3, label='NeuralNetwork')
#plt.plot(published2016point, published2016 , 'bo',lw=3, label='2016antiprotonpaper')
plt.errorbar(published2016point, published2016, yerr=publishederrorbar ,fmt='o',ecolor='r',color='b',elinewidth=2,capsize=4,label='Published (PRL 2016)')
#plt.vlines(16.6, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(38.9, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(147, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(175, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
plt.xlabel('Rigidity(GV)',fontsize=30)
plt.ylabel('Antiproton to proton flux ratio',fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.yscale('log')
plt.grid(True)
plt.legend( loc='best',fontsize=20)
plt.savefig('antiproton_ratio.png')

#################### sta_error #################################################################
sta_error_2016_truevalue = (np.array([0.07, 0.08, 0.10, 0.12, 0.17, 0.26, 0.34, 0.34]) * 10**(-4)).astype(np.float)
sta_error_2016_relative = sta_error_2016_truevalue/published2016[-sta_error_2016_truevalue.shape[0]:]

NN_sta_error_truevalue = (np.array([9.787747327339496e-06, 1.1086034024808252e-05, 1.2340930254898954e-05, 1.4249123852182005e-05, 1.926735965300828e-05 , 2.147968740962006e-05,3.3484072471545556e-05, 3.7355169115658886e-05, 6.232167236847169e-05])).astype(np.float)
NN_sta_error_relative = NN_sta_error_truevalue/NN[-NN_sta_error_truevalue.shape[0]:]

plt.figure(figsize=(18,9))
plt.xlim(0,550)
plt.plot(NNpoint[-NN_sta_error_truevalue.shape[0]:], NN_sta_error_relative*100, 'gs', markersize=10,label='NeuralNetwork')
#plt.plot(published2016point[-sta_error_2016_relative.shape[0]:], sta_error_2016_relative*100, 'bo',markersize=10, label='Published (PRL 2016)')
#plt.vlines(16.6, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(38.9, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(147, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
#plt.vlines(175, 0, max(NN)*1.5, colors = "c", linestyles = "dashed")
plt.xlabel('Rigidity (GV)',fontsize=30)
plt.ylabel('Relative Error [%]',fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.grid(True)
#plt.legend( loc='best',fontsize=20)
plt.savefig('statistical_error.png')


###################################   antiproton number  ##################################################
antiproton_number_published = np.array([15816, 15049, 14426, 13511, 12943, 11723, 10411, 9508, 7876, 7212, 6127, 2697, 2353, 1962, 1772, 1528, 1300, 1143, 1002, 916, 841, 1270, 980, 733, 573, 233, 83, 72, 66])
antiproton_number_fullspan = np.array([182, 121, 111, 124, 110])

plt.figure(figsize=(18,9))
plt.xlim(0,550)
plt.plot(NNpoint[-antiproton_number_fullspan.shape[0]:], antiproton_number_fullspan, 'gs', markersize=10,label='NeuralNetwork')
plt.plot(published2016point[-antiproton_number_published.shape[0]:], antiproton_number_published/4.5*6.5, 'bo',markersize=10, label='Published (PRL 2016)')
plt.vlines(16.6, 0, max(antiproton_number_published), colors = "c", linestyles = "dashed")
plt.vlines(38.9, 0, max(antiproton_number_published), colors = "c", linestyles = "dashed")
plt.vlines(147, 0, max(antiproton_number_published), colors = "c", linestyles = "dashed")
plt.vlines(175, 0, max(antiproton_number_published), colors = "c", linestyles = "dashed")
plt.xlabel('Rigidity (GV)',fontsize=30)
plt.ylabel('Antiproton Numbers',fontsize=30)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.grid(True)
plt.yscale('log')
#plt.legend( loc='best',fontsize=20)
plt.savefig('antiproton_number.png')


















