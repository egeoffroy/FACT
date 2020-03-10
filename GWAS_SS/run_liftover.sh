#!/bin/bash
GWAS=$1
OUT=$2
Rscript ~/liftover_GWAS_SS.R --gwas GWAS -o OUT
