#!/usr/bin/env python
import numpy as np


ratio = np.array([])
binnings = np.array([147, 175, 211, 250, 330, 525])
for binleft in range(binnings.shape[0]-1):
    positive_tem = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/147-1000GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
    negative_tem = np.load('/hpcwork/jara0052/sichen/analysis_6.2/B1042_pr.pl1.flux.l1a9.2016000_7.6_all/147-1000GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
    ratio_tem = float(negative_tem.shape[0]) / float(positive_tem.shape[0])
    ratio = np.append(ratio,ratio_tem)
    print(str(binnings[binleft]))
    print(negative_tem.shape[0])
    print(positive_tem.shape[0])
    print(ratio)







