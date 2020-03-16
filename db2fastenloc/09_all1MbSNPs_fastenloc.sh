#!/bin/bash
gwas_prefix=$1
pop=$2
#run fastenloc with example sumstats
#converted to pips by torus

fastenloc -eqtl ${pop}_all1Mb_fastenloc.eqtl.annotation.vcf.gz -gwas ${gwas_prefix}.gwas.pip.gz -prefix ${pop}_all1Mb_${gwas_prefix}


