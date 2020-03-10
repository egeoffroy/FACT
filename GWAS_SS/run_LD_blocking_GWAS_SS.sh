#!/bin/bash/
ASSOC=$1
LD=$2
OUT=$3
Rscript ~/assign_LD_GWAS_SS.R --assoc ASSOC --LD LD -o OUT
