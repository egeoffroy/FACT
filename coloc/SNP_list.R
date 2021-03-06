#This script pulls the snps from the GWAS Summary Statistics and write them out to another file for making COLOC input
library(dplyr)
library(data.table)
args = commandArgs(trailingOnly=TRUE)
pheno <- args[2]
data <- fread(args[1], header=T, stringsAsFactors=F)
data <- unique(data$variant_id)
write.table(data, paste("GWAS_SNPs_", pheno, ".txt", sep = ''), quote=F, row.names=F, col.names=F)
