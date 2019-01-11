#!/usr/bin/env python
import numpy as np

binnings = np.array([16.6, 18.0, 19.5, 21.1, 22.8, 24.7,26.7,28.8,31.1,33.5,36.1,38.9, 41.9, 45.1, 48.5, 52.2, 56.1, 60.3, 64.8, 69.7, 74.9, 80.5, 93.0, 108.0, 125.0, 147.0])

for binleft in range(binnings.shape[0]-1):
        for trackerpattern in (-1,0,1,2,3,4,5):
		a0=np.array([])
		for i in range(0,2150):
		    a_tem=np.load('positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern'+str(trackerpattern)+'/'+'positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_'+str(trackerpattern)+'_x'+ "%04d" % i +'.npy')
		    if a_tem.shape[0] != 0:
                        if a0.shape[0] == 0:
                            a0=a_tem
                        else:
			    a0=np.row_stack((a0,a_tem))
		fpositive = file('transferdata/positive/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern'+str(trackerpattern)+'/positive_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_'+str(trackerpattern)+'.npy', "wb")
		np.save(fpositive,a0)
		fpositive.close()

                a0=np.array([])
                for i in range(0,2150):
                    a_tem=np.load('negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern'+str(trackerpattern)+'/'+'negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_'+str(trackerpattern)+'_x'+ "%04d" % i +'.npy')
                    if a_tem.shape[0] != 0:
                        if a0.shape[0] == 0:
                            a0=a_tem
                        else:
                            a0=np.row_stack((a0,a_tem))
                fnegative = file('transferdata/negative/'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'GeV/pattern'+str(trackerpattern)+'/negative_'+str(binnings[binleft])+'_'+str(binnings[binleft+1])+'_pattern_'+str(trackerpattern)+'.npy', "wb")
                np.save(fnegative,a0)
                fnegative.close()


