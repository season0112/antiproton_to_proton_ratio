from ROOT import TH2D, TH1D, TCanvas, gPad, TF1, TGraph, gEnv, TFile
from root_numpy import fill_hist
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
plt.switch_backend('agg')




########### data #########################
template_correct=np.load('../../plot_ISS_positive_rigidity.npy')
template_confused=np.load('../../plot_negative_rigidity.npy')
template_electron=np.load('../../electron_negative.npy')
data_negative=np.load('../../plot_ISS_negative_rigidity.npy')
data_positive=np.load('../../plot_ISS_positive_rigidity.npy')

#template_correct=template_correct[0:template_confused.shape[0],:]
#template_electron=template_electron[0:template_confused.shape[0],:]

######## create a graph ###############################
myfile = TFile ('histo.root','new')
TH_template_correct = TH2D("template_correct","template_correct", 100,0,1,100,0.1,1.2);
TH_template_confused = TH2D("template_confused","template_confused", 100,0,1,100,0.1,1.2);
TH_template_electron = TH2D("template_electron","template_electron", 100,0,1,100,0.1,1.2); 
TH_data_negative = TH2D("data_negative","data_negative", 100,0,1,100,0.1,1.2);
TH_data_positive = TH2D("data_positive","data_positive", 100,0,1,100,0.1,1.2);

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

scale = 150/TH_template_correct.Integral()
TH_template_correct.Scale(scale)
scale = 150/TH_template_confused.Integral()
TH_template_confused.Scale(scale)
scale = 150/TH_template_electron.Integral()
TH_template_electron.Scale(scale)


TH_template_correct.Write()
TH_template_confused.Write()
TH_template_electron.Write()
TH_data_negative.Write()
TH_data_positive.Write()


'''
c1 = TCanvas()
gPad.SetGrid()
gPad.SetFrameFillColor(0)
c1.Divide(2,2)
c1.cd(1)
TH_template_correct.Draw('COLZ')
c1.cd(2)
TH_template_confused.Draw('COLZ')
c1.cd(3)
TH_template_electron.Draw('COLZ')
c1.cd(4)
TH_data_negative.Draw('COLZ')
c1.cd()
c1.Update()
c1.SaveAs("hist.emf")
'''




