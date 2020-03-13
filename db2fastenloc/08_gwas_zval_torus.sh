#!/bin/bash

#run torus to get GWAS PIPs from zval file:
#SNP Locus Z-score
gwas_prefix=$1
gzip ${gwas_prefix}.torus.zval.txt
torus -d ${gwas_prefix}.torus.zval.txt.gz --load_zval -dump_pip ${gwas_prefix}.gwas.pip
gzip ${gwas_prefix}.gwas.pip


