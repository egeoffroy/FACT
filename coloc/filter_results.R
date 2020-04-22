# This script filters COLOC results to only include the gene IDs that match the significant genes found by PrediXcan.

library(dplyr)
library(data.table)

"%&%" = function(a,b) paste(a,b,sep="")
args = commandArgs(trailingOnly=TRUE)
pheno <- args[1]
pop <- args[2]
sig_genes_file <- args[3]
coloc_file <- "output_" %&% pheno %&% '_' %&% pop %&% '_coloc.txt.gz'
coloc <- fread(coloc_file, header = T, stringsAsFactors = F)
sig_genes <- fread(sig_genes_file, header = T, stringsAsFactors = F)
sig_genes <- sig_genes$gene
coloc <- coloc %>% filter(gene_id %in% sig_genes)
print(head(coloc))
output <- 'sig_genes_coloc_' %&% pop %&% '_' %&% pheno %&% '.csv'
write.csv(coloc, output, quote = F, row.names=F)
