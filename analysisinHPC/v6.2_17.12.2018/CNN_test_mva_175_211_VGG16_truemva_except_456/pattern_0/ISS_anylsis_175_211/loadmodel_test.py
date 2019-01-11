#!/usr/bin/env python
########################################################################
#                                                                      #
#       Toy Model for Pronton Charge Confusion with Dense Layer        #
#                      version 1.0   07.03.2018                        #
#                                                                      # 
########################################################################


########################## packages ####################################
from __future__ import division
import numpy as np
import math
import json
import collections
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from keras.layers import Activation, Dropout, Flatten, Dense  
from keras.layers import Dense, Conv2D, MaxPooling2D  
from keras.models import Sequential, Model, model_from_json   
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator   
from keras.utils import np_utils
from keras import initializers
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
plt.switch_backend('agg')

########################## Free Parameters #############################
binnumber=150
EcalBDTCut = True
EcalBDTCutvalue_select_proton = 0.0  ## -1 denote proton, 1 denote electron
EcalBDTCutvalue_select_electron = 0.0  ## -1 denote proton, 1 denote electron
TrdProtonHeliumCut = False
TrdProtonHeliumCutValue = 0.3

########################## Properties Label ############################
MvAresult=16
TrdLogLikelihoodRatioProtonHeliumTracker=17

######################### Test events ##################################
testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/147-1000GeV/transferdata/positive/175_211GeV/pattern0/positive_175_211_pattern_0.npy')
testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy')
testset3 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy')
if (EcalBDTCut):
        testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
        testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
        testset3 = testset3[np.where((testset3[:,-5]>-2) & (testset3[:,-5] > EcalBDTCutvalue_select_electron))[0],:]
if (TrdProtonHeliumCut):
        testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
        testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
        testset3 = testset3[np.where(testset3[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]

##################################################################################
testset = np.r_[testset1,testset2,testset3]
testsetMvA = testset[:,MvAresult] ## get the CCProton MvA results
testset = np.expand_dims(testset, axis=2)
inputlist = np.arange(0,16)
testset = testset[:,inputlist,:]
testset[:,4] = np.fabs(testset[:,4])
testset[:,5] = np.fabs(testset[:,5])
testset[:,6] = np.fabs(testset[:,6])
features = 16

##############  model prediction   #################
import CNN_models
model = CNN_models.VGG16(features)
model.load_weights('VGG16.h5')
y_pred = model.predict(testset)

######################## save template data ################################
fplot=file('data/plot_positive_rigidity.npy','wb')
np.save(fplot, np.transpose([ y_pred[0:testset1.shape[0],1], testset1[:,0]])  )
fplot.close()
fplot=file('data/plot_negative_rigidity.npy','wb')
np.save(fplot, np.transpose([ y_pred[testset1.shape[0]:(testset1.shape[0]+testset2.shape[0]),1], testset2[:,0]]) )
fplot.close()
fplot=file('data/electron_negative.npy','wb')
np.save(fplot, np.transpose([ y_pred[(testset1.shape[0]+testset2.shape[0]):,1],  testset3[:,0]]) )
fplot.close()

fplot=file('data/plot_positive_rigidity_CCMVA.npy','wb')
np.save(fplot, np.transpose([ testsetMvA[0:testset1.shape[0]], testset1[:,0] ]))
fplot.close()
fplot=file('data/plot_negative_rigidity_CCMVA.npy','wb')
np.save(fplot, np.transpose([ testsetMvA[testset1.shape[0]:(testset1.shape[0]+testset2.shape[0])], testset2[:,0]]))
fplot.close()
fplot=file('data/electron_negative_CCMVA.npy','wb')
np.save(fplot, np.transpose([ testsetMvA[(testset1.shape[0]+testset2.shape[0]):], testset3[:,0]]))
fplot.close()

'''
########################## NN Prediction ##################################
y_pred = model.predict(testset)

plt.figure(figsize=(18,18))
plt.hist(y_pred[0:testset1.shape[0],1],bins=binnumber,range=(0,1),log=True,alpha=0.5,label='ChargeCorrect',facecolor='blue',edgecolor='black' )
plt.hist(y_pred[testset1.shape[0]:y_pred.shape[0],1],bins=binnumber,range=(0,1),log=True,alpha=0.5,label='ChargeConfused',facecolor='green',edgecolor='black' )
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Estimator $_{CC}$',fontsize=22)
plt.ylabel('Count',fontsize=22)
plt.legend(loc='upper center',fontsize=30)
plt.savefig('plot/ML_test.png')


########################  MvA Prediction ##############################

plt.figure(figsize=(18,18))
plt.hist(testsetMvA[0:testset1.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='ChargeCorrect',facecolor='blue',edgecolor='black'  )
plt.hist(testsetMvA[testset1.shape[0]:y_pred.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='ChargeConfused',facecolor='green',edgecolor='black'  )
plt.xlabel('Estimator $_{CC}$',fontsize=30)
plt.ylabel('Count',fontsize=30)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(loc='upper center',fontsize=30)
plt.savefig('plot/CCMVA_test.png')
'''
