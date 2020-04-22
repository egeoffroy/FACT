#!/bin/bash
geno=$1
pop=$2

python3 05_make_vcf.py --geno ${geno} --pop ${pop}
