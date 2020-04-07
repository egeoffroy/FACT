#!/bin/bash
pop=$1
pheno=$2
pop_size=$3
time python3 summary-gwas-imputation/src/run_coloc.py \
-gwas_mode bse \
-gwas coloc/GWAS_${pop}_${pheno}.txt.gz \
-eqtl_mode bse \
-eqtl coloc/eQTL_${pop}_${pheno}.txt.gz \
-gwas_sample_size FROM_GWAS \
-eqtl_sample_size ${pop_size} \
-parsimony 8 \
-output coloc/output_${pop}_${pheno}_coloc.txt.gz  > /dev/null
