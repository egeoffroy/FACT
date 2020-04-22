#!/bin/bash
pop=$1
python3 04_all1MbSNPs_batch_dapg.py --pop ${pop}
#run batch scan across 32 cores
/usr/local/bin/openmp_wrapper -d ${pop}_all1Mb_batch_dap.cmd -t 16

#Note this took ~7 hrs on 32 cpus
