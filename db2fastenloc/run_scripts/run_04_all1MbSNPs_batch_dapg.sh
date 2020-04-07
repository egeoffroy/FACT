#!/bin/bash
#PBS -N batch_dapg
#PBS -S /bin/bash
#PBS -l walltime=72:00:00
#PBS -l nodes=1:ppn=32
#PBS -l mem=64gb
#PBS -o logs/${PBS_JOBNAME}.o.${PBS_JOBID}.log
#PBS -e logs/${PBS_JOBNAME}.e.${PBS_JOBID}.err
#cd $PBS_O_WORKDIR
pop=$1
python3 04_all1MbSNPs_batch_dapg.py --pop ${pop}
#run batch scan across 32 cores
/usr/local/bin/openmp_wrapper -d ${pop}_all1Mb_batch_dap.cmd -t 4

#Note this took ~7 hrs on 32 cpus
