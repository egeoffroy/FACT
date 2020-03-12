#!/bin/bash

#last step to make eQTL annotation file needed for fastenloc
#-d is a directory that contatins all the dap-g output *fm.out files

perl summarize_dap2enloc.pl -d AFA_all1Mb_dap_out/ -vcf AFA_cposid.vcf.gz | gzip - > AFA_all1Mb_fastenloc.eqtl.annotation.vcf.gz

#next, need to make sure SNP IDs in GWAS match this annotation file
