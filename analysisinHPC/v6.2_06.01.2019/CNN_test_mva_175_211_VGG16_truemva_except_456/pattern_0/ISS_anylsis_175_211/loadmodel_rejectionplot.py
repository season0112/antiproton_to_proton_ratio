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
from ROOT import TH2D, TH1D, TCanvas, gPad, TF1, TGraph, gEnv, TFile, gStyle, TLegend
from root_numpy import fill_hist

########################## Free Parameters #############################
binnumber=300
EcalBDTCut = False
EcalBDTCutvalue_select_proton = 0.0  ## -1 denote proton, 1 denote electron
EcalBDTCutvalue_select_electron = 0.0  ## -1 denote proton, 1 denote electron
TrdProtonHeliumCut = False
TrdProtonHeliumCutValue = 0.3
Testsample = "antiproton233333333333"

########################## Properties Label ############################
MvAresult=16
TrdLogLikelihoodRatioProtonHeliumTracker=17

######################### Test events ##################################
if Testsample is "proton":
        testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/147-1000GeV/transferdata/positive/175_211GeV/pattern0/positive_175_211_pattern_0.npy',encoding="latin1")
        testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")
        testset2 = np.row_stack((testset2,np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")))
        testset1 = testset1[-testset2.shape[0]:,:]
        if (EcalBDTCut):
                testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
                testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
        if (TrdProtonHeliumCut):
                testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
                testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
        

elif Testsample is "antiproton":
        testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_antipr.pl1.1800_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")
        testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_antipr.pl1.1800_7.6_all/147-1000GeV/transferdata/positive/175_211GeV/pattern0/positive_175_211_pattern_0.npy',encoding="latin1")
        testset1 = testset1[-testset2.shape[0]:,:]
        if (EcalBDTCut):
                testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
                testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
        if (TrdProtonHeliumCut):
                testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
                testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]

elif Testsample is "electron":
        testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")
        testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/147-1000GeV/transferdata/positive/175_211GeV/pattern0/positive_175_211_pattern_0.npy',encoding="latin1")
        testset1 = testset1[-testset2.shape[0]:,:]
        if (EcalBDTCut):
                testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_electron))[0],:]
                testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_electron))[0],:]
        if (TrdProtonHeliumCut):
                testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
                testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
else:
        print("Please notify the kind of testsample correctly!")
        testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_antipr.pl1.1800_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")

        testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/147-1000GeV/transferdata/negative/175_211GeV/pattern0/negative_175_211_pattern_0.npy',encoding="latin1")
        testset1 = testset1[-testset2.shape[0]:,:]
##################################################################################
testset = np.r_[testset1,testset2]
testsetMvA = testset[:,MvAresult] ## get the CCProton MvA results
testset = np.expand_dims(testset, axis=2)
inputlist = np.arange(0,16)
testset = testset[:,inputlist,:]
testset[:,4] = np.fabs(testset[:,4])
testset[:,5] = np.fabs(testset[:,5])
testset[:,6] = np.fabs(testset[:,6])
features=16

##############  model prediction   #################
import CNN_models
model = CNN_models.VGG16(features)
model.load_weights('VGG16.h5')
y_pred = model.predict(testset)

######################### fraction plot ################################
protonaccumulatecount=0
fractionoprotonset=np.array([])
for protoniterate in range(binnumber):
        protonaccumulatecount=protonaccumulatecount+np.histogram(y_pred[0:testset1.shape[0],1],binnumber,range=(0,1))[0][binnumber-protoniterate-1]
        fractionoproton=protonaccumulatecount/(testset1.shape[0])
        fractionoprotonset=np.append(fractionoprotonset,fractionoproton)
CCprotonaccumulatecount=0
rejectionCCprotonset=np.array([])
for CCprotoniterate in range(binnumber):
        CCprotonaccumulatecount=CCprotonaccumulatecount+np.histogram(y_pred[testset1.shape[0]:y_pred.shape[0],1],binnumber,range=(0,1))[0][binnumber-CCprotoniterate-1]
        rejectionCCproton=1.0/(CCprotonaccumulatecount/(testset2.shape[0]))
        rejectionCCprotonset=np.append(rejectionCCprotonset,rejectionCCproton)
protonaccumulatecountMvA=0
fractionoprotonsetMvA=np.array([])
for protoniterateMvA in range(binnumber):
        protonaccumulatecountMvA=protonaccumulatecountMvA+np.histogram(testsetMvA[0:testset1.shape[0]],binnumber,range=(0,1))[0][binnumber-protoniterateMvA-1]
        fractionoprotonMvA=protonaccumulatecountMvA/(testset1.shape[0])
        fractionoprotonsetMvA=np.append(fractionoprotonsetMvA,fractionoprotonMvA)
CCprotonaccumulatecountMvA=0
rejectionCCprotonsetMvA=np.array([])
for CCprotoniterateMvA in range(binnumber):
        CCprotonaccumulatecountMvA=CCprotonaccumulatecountMvA+np.histogram(testsetMvA[testset1.shape[0]:y_pred.shape[0]],binnumber,range=(0,1))[0][binnumber-CCprotoniterateMvA-1]
        rejectionCCprotonMvA=1.0/(CCprotonaccumulatecountMvA/(testset2.shape[0]))
        rejectionCCprotonsetMvA=np.append(rejectionCCprotonsetMvA,rejectionCCprotonMvA)
plt.figure(figsize=(18,9))
#plt.ylim(1, rejectionCCprotonsetMvA[0]+2)
plt.plot(fractionoprotonset, rejectionCCprotonset, 'g-',lw=3, label='Neural Network')
plt.plot(fractionoprotonsetMvA, rejectionCCprotonsetMvA, 'b-', lw=3,label='MVA')
plt.xlabel('Efficiency of Proton',fontsize=22)
plt.ylabel('Rejection for CCproton',fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.yscale('log')
plt.legend( loc='best',fontsize=20)
plt.legend( loc='best',fontsize=20)
plt.grid(True)
plt.savefig('fractionfigure.png')

########################## NN Prediction ##################################
plt.figure(figsize=(18,18))
plt.hist(y_pred[0:testset1.shape[0],1],bins=binnumber,range=(0,1),log=True,alpha=0.5,label='ChargeCorrect',facecolor='blue',edgecolor='black' )
plt.hist(y_pred[testset1.shape[0]:y_pred.shape[0],1],bins=binnumber,range=(0,1),log=True,alpha=0.5,label='ChargeConfused',facecolor='green',edgecolor='black' )
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Estimator $_{CC}$',fontsize=22)
plt.ylabel('Count',fontsize=22)
plt.legend(loc='upper center',fontsize=30)
plt.savefig('ML_test.png')

########################  MvA Prediction ##############################
plt.figure(figsize=(18,18))
plt.hist(testsetMvA[0:testset1.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='ChargeCorrect',facecolor='blue',edgecolor='black'  )
plt.hist(testsetMvA[testset1.shape[0]:y_pred.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='ChargeConfused',facecolor='green',edgecolor='black'  )
plt.xlabel('Estimator $_{CC}$',fontsize=30)
plt.ylabel('Count',fontsize=30)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(loc='upper center',fontsize=30)
plt.savefig('CCMVA_test.png')

###################### ROOT PLOT #################################################################################################################
ML_p = TH1D("ML_p","", 100,0,1)
ML_n = TH1D("ML_n","", 100,0,1)
CCMVA_p = TH1D("CCMVA_p","", 100,0,1)
CCMVA_n = TH1D("CCMVA_n","", 100,0,1)

ML_p.SetFillColor(6)
ML_p.SetFillStyle(3004)
ML_p.SetLineColor(6)
ML_n.SetFillColor(4)
ML_n.SetFillStyle(3005)
ML_n.SetLineColor(4)
CCMVA_p.SetFillColor(6)
CCMVA_p.SetFillStyle(3004)
CCMVA_p.SetLineColor(6)
CCMVA_n.SetFillColor(4)
CCMVA_n.SetFillStyle(3005)
CCMVA_n.SetLineColor(4)


fill_hist(ML_p, y_pred[0:testset1.shape[0],1])
fill_hist(CCMVA_p, testsetMvA[0:testset1.shape[0]])
fill_hist(ML_n, y_pred[testset1.shape[0]:y_pred.shape[0],1])
fill_hist(CCMVA_n, testsetMvA[testset1.shape[0]:y_pred.shape[0]])


scale = 150/ML_p.Integral()
ML_p.Scale(scale)
scale = 150/ML_n.Integral()
ML_n.Scale(scale)
scale = 150/CCMVA_p.Integral()
CCMVA_p.Scale(scale)
scale = 150/CCMVA_n.Integral()
CCMVA_n.Scale(scale)


c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
gStyle.SetOptStat("00000000")
ML_p.Draw()
ML_n.Draw('same')
leg =TLegend(.4,.7,.6,.9,)
leg.SetFillColor(0)
leg.AddEntry(ML_p,"Charge Correct")
leg.AddEntry(ML_n,"Charge Confused")
leg.Draw()
ML_p.GetXaxis().SetTitle("Charge Confusion Estimator");
c1.Update()
c1.SaveAs("ML_seperation.pdf")

c2 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
gStyle.SetOptStat("00000000")
CCMVA_p.Draw()
CCMVA_n.Draw('same')
leg =TLegend(.4,.7,.6,.9,)
leg.SetFillColor(0)
leg.AddEntry(ML_p,"Charge Correct")
leg.AddEntry(ML_n,"Charge Confused")
leg.Draw()
CCMVA_p.GetXaxis().SetTitle("Charge Confusion Estimator");
c2.Update()
c2.SaveAs("CCMVA_seperation.pdf")

c3 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
gStyle.SetOptStat("00000000")
ML_p.Draw()
ML_n.Draw('same')
leg =TLegend(.4,.7,.6,.9,)
leg.SetFillColor(0)
leg.AddEntry(ML_p,"Charge Correct")
leg.AddEntry(ML_n,"Charge Confused")
leg.Draw()
ML_p.GetXaxis().SetTitle("Charge Confusion Estimator");
c3.SetLogy()
c3.Update()
c3.SaveAs("ML_seperation_log.pdf")

c4 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
gStyle.SetOptStat("00000000")
CCMVA_p.Draw()
CCMVA_n.Draw('same')
leg =TLegend(.4,.7,.6,.9,)
leg.SetFillColor(0)
leg.AddEntry(ML_p,"Charge Correct")
leg.AddEntry(ML_n,"Charge Confused")
leg.Draw()
CCMVA_p.GetXaxis().SetTitle("Charge Confusion Estimator");
c4.SetLogy()
c4.Update()
c4.SaveAs("CCMVA_seperation_log.pdf")
















