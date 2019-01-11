#!/usr/bin/env python
########################################################################
#                                                                      #
#                           Formatting data                            #
#          from root files to formatted dataset with features          #  
#                      version 5.0   01.03.2018                        #  
#                      update: Additioncal hits                        #  
########################################################################

########################## packages ####################################
from __future__ import division
from ROOT import TFile
from root_numpy import root2array, tree2array
import numpy as np
import sys
import os
import heapq

######################### root to file ################################

treelistname=sys.argv[1]
result = None
with open ('lists/'+treelistname,  "rb") as f:
	lines=f.readlines()
for treecount in range(0,10):
	filename=os.path.basename(lines[treecount].strip())
	myfile = TFile(filename)
	intree = myfile.Get('ExampleAnalysisTree')
	array = tree2array(intree)
	if result is None:
		result = array
	else:
		result = np.append(result,array)

'''
treelistname = str(100)
myfile = TFile('ExampleAnalysis_Tree_00000_00000.root')
intree = myfile.Get('ExampleAnalysisTree')
result = tree2array(intree)
#result=result[0:1000]
'''

############################################  features formatting  ###########################################################
## 1.get features for trainingset. ## 24 tree branches
richbeta=result['RichBeta']
rigidity=result['Rigidity']
pattern=result['Pattern']   
protonCCMVABDT=result['ProtonCCMVABDT']
trdLogLikelihoodRatioProtonHeliumTracker=result['TrdLogLikelihoodRatioProtonHeliumTracker']

trdLogLikelihoodRatioElectronProtonTracker=result['TrdLogLikelihoodRatioElectronProtonTracker']
rigidityAsymmetry=result['RigidityAsymmetry']
rigidityAsymmetryL9=result['RigidityAsymmetryL9']
chi2TrackerYAsymmetry=result['Chi2TrackerYAsymmetry']
innerMaxSpanRigidityMatching=result['InnerMaxSpanRigidityMatching']
l1L9RigidityMatching=result['L1L9RigidityMatching']
l24L58RigidityMatching=result['L24L58RigidityMatching']
log10Chi2TrackerXInner=result['Log10Chi2TrackerXInner']
log10Chi2TrackerYInner=result['Log10Chi2TrackerYInner']
log10Chi2TrackerX=result['Log10Chi2TrackerX']
log10Chi2TrackerY=result['Log10Chi2TrackerY']
trackerL58L24ChargeAsymmetry=result['TrackerL58L24ChargeAsymmetry']
trackerL9Charge=result['TrackerL9Charge']
trackerL78Charge=result['TrackerL78Charge']
upperTofCharge=result['UpperTofCharge']
lowerTofCharge=result['LowerTofCharge']
ecalBDT_EnergyD=result['EcalBDT_EnergyD']
ecalBDT_EnergyD_Smoothed=result['EcalBDT_EnergyD_Smoothed']

## 2. getting np.array data ##
data_formatted=trdLogLikelihoodRatioElectronProtonTracker
data_formatted=np.c_[data_formatted,rigidityAsymmetry,\
rigidityAsymmetryL9,chi2TrackerYAsymmetry,innerMaxSpanRigidityMatching,l1L9RigidityMatching,\
l24L58RigidityMatching,log10Chi2TrackerXInner,log10Chi2TrackerYInner,log10Chi2TrackerX,log10Chi2TrackerY,trackerL58L24ChargeAsymmetry,\
trackerL9Charge,trackerL78Charge,upperTofCharge,lowerTofCharge,\
protonCCMVABDT,trdLogLikelihoodRatioProtonHeliumTracker,ecalBDT_EnergyD,ecalBDT_EnergyD_Smoothed,pattern,richbeta,rigidity]

## 3. applicable & trdheliumproton ##
MVAresult=16
appindex=[]
heliumindex=[]
for count in range(data_formatted.shape[0]):
        if data_formatted[count,MVAresult] == -2:
                appindex.append(count)
allindex = appindex
data_formatted = np.delete (data_formatted, allindex, 0)

## 4.  positive and negative ##
data_formatted_positive=np.array([])
data_formatted_negative=np.array([])
for i in range(data_formatted.shape[0]):
        if data_formatted[i,-1]>0:
                if data_formatted_positive.size:
                        data_formatted_positive=np.row_stack((data_formatted_positive,data_formatted[i,:]))
                else:
                        data_formatted_positive=data_formatted[i,:]
        else:
                if data_formatted_negative.size:
                        data_formatted_negative=np.row_stack((data_formatted_negative,data_formatted[i,:]))
                else:
                        data_formatted_negative=data_formatted[i,:]

## 5. split ## 
binnings = np.array([16.6, 18.0, 19.5, 21.1, 22.8, 24.7,26.7,28.8,31.1,33.5,36.1,38.9, 41.9, 45.1, 48.5, 52.2, 56.1, 60.3, 64.8, 69.7, 74.9, 80.5, 93.0, 108.0, 125.0, 147.0])
for binleft in range(binnings.shape[0]-1):
        locals()['index_p_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])] = []
	for i in range(data_formatted_positive.shape[0]):
		if data_formatted_positive[i,-1] < binnings[binleft] or data_formatted_positive[i,-1]> binnings[binleft+1] :
			locals()['index_p_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])].append(i)
        p_tem = np.delete(data_formatted_positive, locals()['index_p_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])], 0)
        print('p_tem'+str(binnings[binleft])+'to'+str(binnings[binleft+1])+':'+str(p_tem.shape))
	pattern0p=np.array([])
	for j in range(p_tem.shape[0]):
	    if p_tem[j,-3] == 0:
		if pattern0p.shape[0] == 0:
		    pattern0p = p_tem[j,:]
		else:
		    pattern0p = np.row_stack((pattern0p, p_tem[j,:]))
	f = file('rawdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+ str(binnings[binleft]) +'_'+ str(binnings[binleft+1]) +'_pattern_0_'+treelistname+'.npy','wb')
	np.save(f,pattern0p)
	f.close()
        print('pattern0p:'+ str(pattern0p.shape))

        locals()['index_n_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])] = []
        for i in range(data_formatted_negative.shape[0]):
                if data_formatted_negative[i,-1] > -binnings[binleft] or data_formatted_negative[i,-1] < -binnings[binleft+1] :
                        locals()['index_n_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])].append(i)
        n_tem = np.delete(data_formatted_negative, locals()['index_n_' + str(binnings[binleft]) + '_' + str(binnings[binleft+1])], 0)
        print('n_tem'+str(binnings[binleft])+'to'+str(binnings[binleft+1])+':'+str(n_tem.shape))
        pattern0n=np.array([])
        for j in range(n_tem.shape[0]):
            if n_tem[j,-3] == 0:
                if pattern0n.shape[0] == 0:
                    pattern0n = n_tem[j,:]
                else:
                    pattern0n = np.row_stack((pattern0n, n_tem[j,:]))
        f = file('rawdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+ str(binnings[binleft]) +'_'+ str(binnings[binleft+1]) +'_pattern_0_'+treelistname+'.npy','wb')
        np.save(f,pattern0n)
        f.close()
        print('pattern0n:'+ str(pattern0n.shape))





















