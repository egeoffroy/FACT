#!/bin/bash

#run torus to get GWAS PIPs from zval file:
#SNP Locus Z-score

gzip Wojcik_height.torus.zval.txt
torus -d Wojcik_height.torus.zval.txt.gz --load_zval -dump_pip Wojcik_height.gwas.pip
gzip Wojcik_height.gwas.pip

gzip Wojcik_WBC.torus.zval.txt
torus -d Wojcik_WBC.torus.zval.txt.gz --load_zval -dump_pip Wojcik_WBC.gwas.pip
gzip Wojcik_WBC.gwas.pip
