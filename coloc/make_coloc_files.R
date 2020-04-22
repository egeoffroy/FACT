#This script formats the eQTL and GWAS data for COLOC input

library(data.table)
library(dplyr)
library(R.utils)
print(getwd())

"%&%" = function(a,b) paste(a,b,sep="")

args = commandArgs(trailingOnly=TRUE) #get arguments
phenofile <- args[1]
frqfile <- args[2]
phenos <- args[3]
pop <- args[4]
pop_sample_size <- args[5]
#print('Population Size: ' pop_sample_size)
meqtlfile <- args[6]

chrs <- c(1:22)

sig_gene_SNPs <- fread(paste("GWAS_SNPs_", phenos, ".txt", sep = ''), header = F) #get SNPs from GWAS
sig_gene_SNPs <- sig_gene_SNPs$V1

  frq <- fread(frqfile)
  frq <- frq %>% dplyr::select(SNP, MAF)

  for(pheno in phenos){ #read in GEMMA output file
    GEMMA_result <- fread(phenofile, header = T)
    n <- GEMMA_result$n[2]
    GEMMA_result$chr_pos <- paste(gsub("chr", "", GEMMA_result$chromosome), GEMMA_result$ps, sep = ":")
    GEMMA_for_COLOC <- GEMMA_result %>% dplyr::select(variant_id, beta, standard_error, effect_allele_frequency) #subset to COLOC input
    GEMMA_for_COLOC$sample_size <- n
    colnames(GEMMA_for_COLOC) <- c("panel_variant_id", "effect_size", "standard_error", "frequency", "sample_size")
    GEMMA_for_COLOC <- GEMMA_for_COLOC[complete.cases(GEMMA_for_COLOC),] #COLOC does not like missing values
    GWAS_write <- GEMMA_for_COLOC
    eQTL_write <- data.frame(gene_id = character(), variant_id = character(), maf = numeric(), pval_nominal = numeric(), slope = numeric(), slope_se = numeric(), stringsAsFactors = F)

    for(chr in chrs){
      if(pop == 'AFA' || pop == 'AFHI' || pop == 'HIS' || pop == 'CAU' || pop == 'ALL'){
         system("zcat -f /home/wheelerlab3/files_for_revisions_plosgen/meqtl_results/MESA/" %&% pop %&% "_Nk_10_PFs_chr" %&% chr %&% "pcs_3.meqtl.cis.* > coloc/meQTL_" %&% pop %&% "_input.txt") #fread doesn't seem to like wildcards so we're gonna do this the ugly way
         meqtlfile <- "coloc/meQTL_" %&% pop %&% "_input.txt"
      }
      meqtl <- fread(meqtlfile, nThread = 40) #read in matrix eQTL results
      meqtl$se <- meqtl$beta / meqtl$statistic #make your own standard error since it's not in the meQTL output
      meqtl$n_samples <- pop_sample_size
      meQTL_for_COLOC <- left_join(meqtl, frq, by = c("snps" = "SNP")) #add freq to COLOC input
      meQTL_for_COLOC <- meQTL_for_COLOC %>% dplyr::select(gene, snps, MAF, pvalue, beta, se) #subset to COLOC input
      colnames(meQTL_for_COLOC) <- c("gene_id", "variant_id", "maf", "pval_nominal", "slope", "slope_se")
      meQTL_for_COLOC <- meQTL_for_COLOC[complete.cases(meQTL_for_COLOC),]

      eQTL_write <- rbind(eQTL_write, meQTL_for_COLOC)
    }

    snps_in_both <- intersect(GWAS_write$panel_variant_id, eQTL_write$variant_id) 
    snps_in_all <- intersect(snps_in_both, sig_gene_SNPs)
    GWAS_write <- subset(GWAS_write, panel_variant_id %in% snps_in_all)
    eQTL_write <- subset(eQTL_write, variant_id %in% snps_in_all)
    eQTL_write <- eQTL_write[order(eQTL_write$gene_id),]

    fwrite(eQTL_write, "coloc/eQTL_" %&% pop %&% "_" %&% pheno %&% ".txt", quote = F, sep = "\t", na = "NA", row.names = F, col.names = T)
    gzip("coloc/eQTL_" %&% pop %&% "_" %&% pheno %&% ".txt", destname = "coloc/eQTL_" %&% pop %&% "_" %&% pheno %&% ".txt.gz") #script may only take .gz values so can't hurt to be too careful
    fwrite(GWAS_write, "coloc/GWAS_" %&% pop %&% "_" %&% pheno %&% ".txt", row.names = F, col.names = T, sep = "\t", quote = F, na = "NA")
    gzip("coloc/GWAS_" %&% pop %&% "_" %&% pheno %&% ".txt", "coloc/GWAS_" %&% pop %&% "_" %&% pheno %&% ".txt.gz")
    print("Completed with " %&% pop %&% ", for " %&% pheno %&% ".")
  }
}
