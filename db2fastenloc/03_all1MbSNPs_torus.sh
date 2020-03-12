#!/bin/bash

#run torus to get SNP priors based on distance to gene and
#BFs from previous step

#make snp.map file, want varID chr pos
for i in {1..22}
do
    awk '{print $3 "\t" $1 "\t" $2}' /home/wheelerlab3/files_for_revisions_plosgen/en_v7/prepare_data/genotypes/AFA_${i}_annot.txt >> AFA.snp.map
done
#rm lines with header & gzip
grep -v varID AFA.snp.map | gzip > AFA.snp.map.gz
rm AFA.snp.map

#make gene.map file want gene_id chr start end
for i in {1..22}
do
    awk '{print $2 "\t" $1 "\t" $4 "\t" $5}' /home/wheelerlab3/files_for_revisions_plosgen/en_v7/prepare_data/expression/gencode.v18.annotation.parsed.txt >> AFA.gene.map
done
#rm lines with header & gzip
grep -v gene_id AFA.gene.map | gzip > AFA.gene.map.gz
rm AFA.gene.map

torus -d AFA.all1Mb.bf.gz -smap AFA.snp.map.gz -gmap AFA.gene.map.gz --load_bf -dump_prior AFA_all1Mb_priors

#this gives different priors based on position, but assumes
#position in third column is the TSS (it could be TES for some genes)
#probably won't affect results too much since we go 1Mb in both directions (and genes aren't that big)
