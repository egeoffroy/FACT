#!/bin/bash

#last step to make eQTL annotation file needed for fastenloc
#-d is a directory that contatins all the dap-g output *fm.out files
pop=$1
perl summarize_dap2enloc.pl -d ${pop}_all1Mb_dap_out/ -vcf ${pop}_cposid.vcf.gz | gzip - > ${pop}_all1Mb_fastenloc.eqtl.annotation.vcf.gz

#next, need to make sure SNP IDs in GWAS match this annotation file


