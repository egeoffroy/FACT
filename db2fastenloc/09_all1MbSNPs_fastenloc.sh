#!/bin/bash

#run fastenloc with example sumstats
#converted to pips by torus

fastenloc -eqtl AFA_all1Mb_fastenloc.eqtl.annotation.vcf.gz -gwas Wojcik_height.gwas.pip.gz -prefix AFA_all1Mb_Wojcik_height

fastenloc -eqtl AFA_all1Mb_fastenloc.eqtl.annotation.vcf.gz -gwas Wojcik_WBC.gwas.pip.gz -prefix AFA_all1Mb_Wojcik_WBC
