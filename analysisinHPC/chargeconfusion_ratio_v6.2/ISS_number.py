import numpy as np

binnings = np.array([36.1, 38.9, 41.9])
for binleft in range(binnings.shape[0]-1):
    positive_tem = np.load('/hpcwork/jara0052/sichen/analysis_6.2/ISS/16.6-147GeV/transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
    negative_tem = np.load('/hpcwork/jara0052/sichen/analysis_6.2/ISS/16.6-147GeV/transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern0/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_0.npy')
    print(str(binnings[binleft]))
    print(negative_tem.shape[0])
    print(positive_tem.shape[0])

'''
fplot=file('ccratio.npy','wb')
np.save(fplot,ratio)
fplot.close()
'''


