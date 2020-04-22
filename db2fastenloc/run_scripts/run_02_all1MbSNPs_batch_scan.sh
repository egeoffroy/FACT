#!/bin/bash
pop=$1
mkdir ${pop}_all1Mb_scan_out
python3 02_all1MbSNPs_batch_scan.py --pop ${pop}
#run batch scan across 32 cores
/usr/local/bin/openmp_wrapper -d ${pop}_all1Mb_batch_scan.cmd -t 32
#combine output files
python3 02b_concat_scan_out_bf_files.py --pop ${pop}
#Note this took ~7.5 hrs on 32 cpus
