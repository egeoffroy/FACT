#!/bin/Rscript
#Find beta and SE columns in each GWAS Summary Statistics file
library(data.table)
library(dplyr)

args = commandArgs(trailingOnly=TRUE)
find_beta_se <- function(x){
        data <- fread(x, header=T, stringsAsFactors=F)
        names_data <- names(data)
        beta <- grep("beta", names_data)-1
        if(length(beta) == 0){
                beta <- grep("Beta", names_data)-1
        }
        se <- grep("standard_error", names_data)-1
        if(length(se) == 0){
                se <- grep("SE", names_data)-1
        }
        #col_list <- c(beta, se)
        chr <- grep("chr" , names_data)-1
        if(length(chr) ==0){
                chr <- grep("chromosome", names_data)-1
        }
        if(length(chr) ==0){
                chr <- grep("chrom", names_data)-1
        }
        oa <- grep("other_allele" , names_data)-1
        if(length(oa) ==0){                                                                                             
                oa <- grep("allele2", names_data)-1
        }
        ae <- grep("effect_allele" , names_data)-1
        if(length(ae) ==0){
                ae <- grep("allele1", names_data)-1
        }
        bp <- grep("bp", names_data)-1
        if(length(bp) == 0){
                bp <- grep("base_position", names_data)-1
                if(length(bp)==0){
                        bp <- grep("pos", names_data)-1
                }
                if(length(bp)==0){
                        bp <- grep("base_pair_location", names_data)-1
                }
        }
        col_list <- c(beta, se, chr, bp, oe, ae)
        return(col_list)
}

write.csv(find_beta_se(args[1]), "column_numbers.csv", quote = F, row.names=F)
