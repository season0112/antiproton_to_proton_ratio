#! /usr/bin/env zsh
#BSUB -J toymodel_analysis6.py
#BSUB -o /rwthfs/rz/cluster/home/bo791269/neuralnetwork_v6.2/v6.2_17.12.2018/CNN_test_mva_16.6_80.5_VGG16_truemva_except_456/pattern_0/output/output_00000.txt
#BSUB -W 6:00
#BSUB -M 51200
#BSUB -C 0
#BSUB -P "jara0052"
#BSUB -R "pascal"
#BSUB -gpu "num=2"
#BSUB -m c24m128
#BSUB -R "select[hpcwork_fast]"
#BSUB -R "select[cvmfs]"

source /rwthfs/rz/cluster/home/bo791269/neuralnetwork_v6.2/v6.2_17.12.2018/CNN_test_mva_16.6_80.5_VGG16_truemva_except_456/pattern_0/sandbox/environment.sh

toymodel_analysis6.py 
RET=${?}
echo
echo job 00000 exited with return code ${RET}

exit ${RET}
