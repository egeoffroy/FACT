#!/bin/bash
#PBS -N make_vcf
#PBS -S /bin/bash
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=4
#PBS -l mem=16gb
#PBS -o logs/${PBS_JOBNAME}.o.${PBS_JOBID}.log
#PBS -e logs/${PBS_JOBNAME}.e.${PBS_JOBID}.err
#cd $PBS_O_WORKDIR
geno=$1
pop=$2

python3 05_make_vcf.py --geno ${geno} --pop ${pop}
