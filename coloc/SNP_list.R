#This script pulls the snps from the GWAS Summary Statistics
library(dplyr)
library(data.table)
args = commandArgs(trailingOnly=TRUE)
pheno <- args[2]
data <- fread(args[1], header=T, stringsAsFactors=F)
cat(data$n[2])
data <- unique(data$variant_id)
write.table(data, paste("GWAS_SNPs", pheno, ".txt", sep = ''), quote=F, row.names=F, col.names=F)
