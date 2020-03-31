#!/bin/bash
pop=$1
gwas=$2
pheno=$3
frq=$4
python3 coloc_pipeline_main.py --pheno_id ${pheno} --pop ${pop} --gwas_SS ${gwas} --frq ${frq}
