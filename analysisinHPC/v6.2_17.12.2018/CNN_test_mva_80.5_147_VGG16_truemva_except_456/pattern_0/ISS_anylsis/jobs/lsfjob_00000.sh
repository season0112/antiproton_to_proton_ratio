#! /usr/bin/env zsh
#BSUB -J loadmodel_ISS.py
#BSUB -o /lustren/hpcwork/bo791269/neuralnetwork_v6.2/v6.2_17.12.2018/CNN_test_mva_80.5_147_VGG16_truemva_except_456/pattern_0/ISS_anylsis/output/output_00000.txt
#BSUB -W 6:00
#BSUB -M 51200
#BSUB -C 0
#BSUB -P "jara0052"
#BSUB -R "pascal"
#BSUB -gpu "num=2"
#BSUB -m c24m128
#BSUB -R "select[hpcwork_fast]"
#BSUB -R "select[cvmfs]"

source /lustren/hpcwork/bo791269/neuralnetwork_v6.2/v6.2_17.12.2018/CNN_test_mva_80.5_147_VGG16_truemva_except_456/pattern_0/ISS_anylsis/sandbox/environment.sh

loadmodel_ISS.py 
RET=${?}
echo
echo job 00000 exited with return code ${RET}

exit ${RET}
