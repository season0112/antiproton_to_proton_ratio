from ROOT import TH2D, TH1D, TCanvas, gPad, TF1, TGraph, gEnv, TFile
from root_numpy import fill_hist
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
plt.switch_backend('agg')

##################### data ####################################################
template_correct=np.load('../../plot_ISS_positive_rigidity36.1_38.9.npy')
template_confused=np.load('../../plot_negative_rigidity36.1_38.9.npy')
template_electron=np.load('../../electron_negative36.1_38.9.npy')
data_negative=np.load('../../plot_ISS_negative_rigidity36.1_38.9.npy')
data_positive=np.load('../../plot_ISS_positive_rigidity36.1_38.9.npy')
'''
################ remove of charge confused events initiallly ###################
template_correct = template_correct[np.where(template_correct[:,0]>0.2)[0],:]
template_confused = template_confused[np.where(template_confused[:,0]>0.2)[0],:]
template_electron = template_electron[np.where(template_electron[:,0]>0.2)[0],:]
data_negative = data_negative[np.where(data_negative[:,0]>0.2)[0],:]
data_positive = data_positive[np.where(data_positive[:,0]>0.2)[0],:]
'''
'''
################ TrdLikelihood cut #####################
template_correct = template_correct[np.where(template_correct[:,1]>0.8)[0],:]
template_confused = template_confused[np.where(template_confused[:,1]>0.8)[0],:]
template_electron = template_electron[np.where(template_electron[:,1]>0.8)[0],:]
data_negative = data_negative[np.where(data_negative[:,1]>0.8)[0],:]
data_positive = data_positive[np.where(data_positive[:,1]>0.8)[0],:]
'''
'''
################ CC estimator cut #####################
template_correct = template_correct[np.where(template_correct[:,0]>0.9)[0],:]
template_confused = template_confused[np.where(template_confused[:,0]>0.9)[0],:]
template_electron = template_electron[np.where(template_electron[:,0]>0.9)[0],:]
data_negative = data_negative[np.where(data_negative[:,0]>0.9)[0],:]
data_positive = data_positive[np.where(data_positive[:,0]>0.9)[0],:]
'''
######## create a graph ###############################
CCbinningnumber = 20
TRDbinningnumber = 12
 
myfile = TFile ('histo.root','new')
TH_template_correct = TH2D("template_correct","Antiproton", CCbinningnumber,0,1,TRDbinningnumber,0.1,1.5);
TH_template_confused = TH2D("template_confused","Charge Confused Proton", CCbinningnumber,0,1,TRDbinningnumber,0.1,1.5);
TH_template_electron = TH2D("template_electron","Electron", CCbinningnumber,0,1,TRDbinningnumber,0.1,1.5); 
TH_data_negative = TH2D("data_negative","Negative Rigidity Events", CCbinningnumber,0,1,TRDbinningnumber,0.1,1.5);
TH_data_positive = TH2D("data_positive","Positive Rigidity Events", CCbinningnumber,0,1,TRDbinningnumber,0.1,1.5);

TH_template_correct.Sumw2()
TH_template_confused.Sumw2()
TH_template_electron.Sumw2()
TH_data_negative.Sumw2()
TH_data_positive.Sumw2()

fill_hist(TH_template_correct, template_correct)
fill_hist(TH_template_confused, template_confused)
fill_hist(TH_template_electron, template_electron)
fill_hist(TH_data_negative, data_negative)
fill_hist(TH_data_positive, data_positive)

scale = 1/TH_template_correct.Integral()
TH_template_correct.Scale(scale)
scale = 1/TH_template_confused.Integral()
TH_template_confused.Scale(scale)
scale = 1/TH_template_electron.Integral()
TH_template_electron.Scale(scale)


TH_template_correct.Write()
TH_template_confused.Write()
TH_template_electron.Write()
TH_data_negative.Write()
TH_data_positive.Write()


c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
TH_template_correct.Draw('COLZ')
TH_template_correct.SetStats(0)
TH_template_correct.GetXaxis().SetTitle("#bf{Charge Confusion Estimator}")
TH_template_correct.GetYaxis().SetTitle("#bf{TrdLikelihood}")
c1.Update()
c1.SaveAs("correct.pdf")


c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
TH_template_confused.Draw('COLZ')
TH_template_confused.SetStats(0)
TH_template_confused.GetXaxis().SetTitle("#bf{Charge Confusion Estimator}")
TH_template_confused.GetYaxis().SetTitle("#bf{TrdLikelihood}")
c1.Update()
c1.SaveAs("confused.pdf")

c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
TH_template_electron.Draw('COLZ')
TH_template_electron.SetStats(0)
TH_template_electron.GetXaxis().SetTitle("#bf{Charge Confusion Estimator}")
TH_template_electron.GetYaxis().SetTitle("#bf{TrdLikelihood}")
c1.Update()
c1.SaveAs("electron.pdf")


c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
TH_data_negative.Draw('COLZ')
TH_data_negative.SetStats(0)
TH_data_negative.GetXaxis().SetTitle("#bf{Charge Confusion Estimator}")
TH_data_negative.GetYaxis().SetTitle("#bf{TrdLikelihood}")
c1.Update()
c1.SaveAs("data_negative.pdf")



