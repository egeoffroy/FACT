#!/bin/bash

#run torus to get SNP priors based on distance to gene and
#BFs from previous step
geno_path=$1
genemapfile=$2
pop=$3
#make snp.map file, want varID chr pos
for i in {1..22}
do
    awk '{print $3 "\t" $1 "\t" $2}' ${geno_path}${pop}_${i}_annot.txt >> ${pop}.snp.map
done
#rm lines with header & gzip
grep -v varID ${pop}.snp.map | gzip > ${pop}.snp.map.gz
rm ${pop}.snp.map

#make gene.map file want gene_id chr start end
for i in {1..22}
do
    awk '{print $2 "\t" $1 "\t" $4 "\t" $5}' ${genemapfile} >> ${pop}.gene.map
done
#rm lines with header & gzip
grep -v gene_id ${pop}.gene.map | gzip > ${pop}.gene.map.gz
rm ${pop}.gene.map

torus -d ${pop}.all1Mb.bf.gz -smap ${pop}.snp.map.gz -gmap ${pop}.gene.map.gz --load_bf -dump_prior ${pop}_all1Mb_priors

#this gives different priors based on position, but assumes
#position in third column is the TSS (it could be TES for some genes)
#probably won't affect results too much since we go 1Mb in both directions (and genes aren't that big)
