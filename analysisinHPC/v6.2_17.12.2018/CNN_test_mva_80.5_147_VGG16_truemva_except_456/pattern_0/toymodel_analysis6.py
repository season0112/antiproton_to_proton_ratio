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
from keras.layers import Activation, Dropout, Flatten, Dense  
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D,ZeroPadding1D,Convolution1D 
from keras.models import Sequential, Model, model_from_json   
from keras.optimizers import SGD, RMSprop, Adam
from keras.preprocessing.image import ImageDataGenerator   
from keras.utils import np_utils
from keras import initializers
from keras.applications.resnet50 import ResNet50
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
plt.switch_backend('agg')

binnings = np.array([80.5, 93.0, 108.0, 125.0, 147.0])
for binleft in range(binnings.shape[0]-1):

	########################## Free Parameters #############################
	epochsnumber = 22
	batchsize = 1000
	binnumber = 80
	#learningrate = 0.0000005
	#learningrate = 0.000001
	#learningrate = 0.000005
	#learningrate = 0.00001
	learningrate = 0.00005
	#learningrate = 0.0001
	#learningrate = 0.001

	loadweights = False
	EcalBDTCut = False
	EcalBDTCutvalue_select_proton = 0.0  ## -1 denote proton, 1 denote electron
	EcalBDTCutvalue_select_electron = 0.0  ## -1 denote proton, 1 denote electron
	TrdProtonHeliumCut = False
	TrdProtonHeliumCutValue = 0.3
	Testsample = "proton"

	########################## Properties Label ############################
	MvAresult = 16
	TrdLogLikelihoodRatioProtonHeliumTracker=17

	################### load data and features #############################
	positiveprotonB1042 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
	CCprotonB1042 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
	positiveprotonB1042 = positiveprotonB1042[0:CCprotonB1042.shape[0],:]
	electronpositive = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
	electronnegative = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
	electronpositive = electronpositive[0:CCprotonB1042.shape[0],:]
	electronnegative = electronnegative[0:CCprotonB1042.shape[0],:]
	if (EcalBDTCut):
		positiveprotonB1042=positiveprotonB1042[np.where((positiveprotonB1042[:,-5]>-2) & (positiveprotonB1042[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
		CCprotonB1042=CCprotonB1042[np.where((CCprotonB1042[:,-5]>-2) & (CCprotonB1042[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
		electronpositive = electronpositive[np.where((electronpositive[:,-5]>-2) & (electronpositive[:,-5] > EcalBDTCutvalue_select_electron))[0],:]
		electronnegative = electronnegative[np.where((electronnegative[:,-5]>-2) & (electronnegative[:,-5] > EcalBDTCutvalue_select_electron))[0],:]
	if (TrdProtonHeliumCut):
		positiveprotonB1042 = positiveprotonB1042[np.where(positiveprotonB1042[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
		CCprotonB1042 = CCprotonB1042[np.where(CCprotonB1042[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
		electronpositive = electronpositive[np.where(electronpositive[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
		electronnegative = electronnegative[np.where(electronnegative[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
	correct = np.row_stack((positiveprotonB1042,electronnegative)) 
	confused = np.row_stack((CCprotonB1042,electronpositive))

	########################## Target Sample ############################
	trainingset = np.r_[correct,confused]
	y_proton = [1]*correct.shape[0]
	y_CCproton = [0]*confused.shape[0]
	y_target = np.array(y_proton+y_CCproton)
	y_target = np_utils.to_categorical(y_target, num_classes=2)

	######################### Test events ##################################
	if Testsample is "proton":
		testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1o9.2016000_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset2 = np.row_stack((testset2,np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")))
		testset1 = testset1[-testset2.shape[0]:,:]
		if (EcalBDTCut):
			testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
			testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
		if (TrdProtonHeliumCut):
			testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
			testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]

	elif Testsample is "antiproton":
		testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_antipr.pl1.1800_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_antipr.pl1.1800_7.6_all/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset1 = testset1[-testset2.shape[0]:,:]
		if (EcalBDTCut):
			testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
			testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] < EcalBDTCutvalue_select_proton))[0],:]
		if (TrdProtonHeliumCut):
			testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
			testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]

	elif Testsample is "electron":
		testset1 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset2 = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1091_el.pl1.0_25200_7.6_all/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy',encoding="latin1")
		testset1 = testset1[-testset2.shape[0]:,:]
		if (EcalBDTCut):
			testset1 = testset1[np.where((testset1[:,-5]>-2) & (testset1[:,-5] > EcalBDTCutvalue_select_electron))[0],:]
			testset2 = testset2[np.where((testset2[:,-5]>-2) & (testset2[:,-5] > EcalBDTCutvalue_select_electron))[0],:]
		if (TrdProtonHeliumCut):
			testset1 = testset1[np.where(testset1[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
			testset2 = testset2[np.where(testset2[:,TrdLogLikelihoodRatioProtonHeliumTracker] < TrdProtonHeliumCutValue)[0],:]
	else:
		print("Please notify the kind of testsample correctly!")



	######################### Test Target Sample  ##########################
	testset = np.r_[testset1,testset2]
	testsetMvA = testset[:,MvAresult] ## get the CCProton MvA results
	testset1_pre = [1]*len(testset1)
	testset2_pre = [0]*len(testset2)
	testset_pre = np.array(testset1_pre+testset2_pre)
	testset_pre = np_utils.to_categorical(testset_pre, num_classes=2)

	####################### training data shuffling ########################
	indices = np.arange(len(trainingset))
	np.random.shuffle(indices)
	trainingset = trainingset[indices]
	y_target = y_target[indices]

	################  add a axis for convolutional 1D ######################
	trainingset = np.expand_dims(trainingset, axis=2)
	testset = np.expand_dims(testset, axis=2)

	################  which features are used ###############################
	inputlist = np.arange(0,16)
	trainingset = trainingset[:,inputlist] 
	testset = testset[:,inputlist]
	trainingset[:,4] = np.fabs(trainingset[:,4])
	testset[:,4] = np.fabs(testset[:,4])
	trainingset[:,5] = np.fabs(trainingset[:,5])
	testset[:,5] = np.fabs(testset[:,5])
	trainingset[:,6] = np.fabs(trainingset[:,6])
	testset[:,6] = np.fabs(testset[:,6])
	features = 16

	##################### model and compile #################################
	import CNN_models
	model = CNN_models.VGG16(features)
	if (loadweights): 
	    model.load_weights('weight/VGG16_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'.h5')
	opt = RMSprop(lr=learningrate, rho=0.9, epsilon=1e-6)
	opt2 = SGD(lr=learningrate, momentum=0.9, nesterov=True)
	opt3 = Adam(lr=learningrate, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
	model.compile(optimizer=opt3,
		      loss='categorical_crossentropy',
		      metrics=['accuracy'])
	model.summary()

	######################### Train the model, #############################
	history = model.fit(trainingset, y_target, 
			    epochs=epochsnumber, 
			    batch_size=batchsize,
			    validation_data=(testset,testset_pre))

	########################## Prediction ##################################
	y_pred = model.predict(testset)  
	protonpred = 0
	CCprotonpred = 0
	for protonpredcount in range(testset1.shape[0]):
		if np.argmax(y_pred[protonpredcount])==1:
			protonpred+=1
	for CCprotonpredcount in range(testset1.shape[0],y_pred.shape[0]):	
		if np.argmax(y_pred[CCprotonpredcount])==0:
			CCprotonpred+=1
	print("ChargeConrrect Prediction:"+str(protonpred)+" out of "+str(testset1.shape[0]))
	print("ChargeConfused Prediction:"+str(CCprotonpred)+" out of "+str(testset2.shape[0]))	

	######################### model weights ################################
	model.save_weights('weight/VGG16_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'.h5')

	################## Plot Loss and Accuracy Prediction ###################
	plt.figure(figsize=(18,18))
	plt.subplot(221)
	loss = history.history['loss']
	val_loss = history.history['val_loss']
	epochs = range(1, len(loss) + 1)
	plt.plot(epochs, loss, 'bo', label='Training loss')
	plt.plot(epochs, val_loss, 'b', label='Validation loss')
	plt.title('Training and validation loss',fontsize=26)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel('Epochs',fontsize=22)
	plt.ylabel('Loss',fontsize=22)
	plt.legend(loc='best',fontsize=20)
	plt.subplot(222)
	acc = history.history['acc']
	val_acc = history.history['val_acc']
	plt.plot(epochs, acc, 'bo', label='Training acc')
	plt.plot(epochs, val_acc, 'b', label='Validation acc')
	plt.title('Training and validation accuracy',fontsize=26)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel('Epochs',fontsize=22)
	plt.ylabel('Accuracy',fontsize=22)
	plt.legend(loc='best',fontsize=20)
	plt.subplot(223)
	plt.hist(y_pred[0:testset1.shape[0],1],bins=binnumber,range=(0,1),log=True ) 
	plt.title("Proton",fontsize=26) 
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel('Estimator $_{CC}$',fontsize=22)
	plt.ylabel('Count',fontsize=22)
	plt.subplot(224)
	plt.hist(y_pred[testset1.shape[0]:y_pred.shape[0],1],bins=binnumber,range=(0,1),log=True ) 
	plt.title("CCProton",fontsize=26) 
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel('Estimator $_{CC}$',fontsize=22)
	plt.ylabel('Count',fontsize=22)
	plt.savefig('plot/ML'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'.png')

	######################## Plot MvA results ##############################
	protonMvApred = 0
	CCprotonMvApred = 0
	for protonMvApredcount in range(testset1.shape[0]):
		if testsetMvA[protonMvApredcount]>0.5:
			protonMvApred+=1		
	for CCprotonMvApredcount in range(testset1.shape[0],y_pred.shape[0]):	
		if testsetMvA[CCprotonMvApredcount]<0.5:
			CCprotonMvApred+=1
	plt.figure(figsize=(18,18))
	plt.hist(testsetMvA[0:testset1.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='Proton',facecolor='blue',edgecolor='black'  )
	plt.hist(testsetMvA[testset1.shape[0]:y_pred.shape[0]],binnumber,range=(0,1),log=True, alpha=0.5,label='CCProton',facecolor='green',edgecolor='black'  ) 
	plt.xlabel('Estimator $_{CC}$',fontsize=30)
	plt.ylabel('Count',fontsize=30)
	plt.xticks(fontsize=25)
	plt.yticks(fontsize=25)
	plt.legend(loc='upper center',fontsize=30)
	plt.savefig('plot/CCMVA'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'.png')

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
	plt.plot(fractionoprotonset, rejectionCCprotonset, 'g-',lw=3, label='Neurual Network')
	plt.plot(fractionoprotonsetMvA, rejectionCCprotonsetMvA, 'b-', lw=3,label='MVA')
	plt.xlabel('Efficiency of Proton',fontsize=22)
	plt.ylabel('Rejection for CCproton',fontsize=22)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.yscale('log')
	plt.legend( loc='best',fontsize=20)
	plt.savefig('plot/fractionfigure'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'.png')

