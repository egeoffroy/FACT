#!/bin/Rscript
#Find beta and SE columns in each GWAS Summary Statistics file
library(data.table)

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
        col_list <- c(beta, se)
        return(col_list)
}

write.csv(find_beta_se(args[1]), "column_numbers.csv", quote = F, row.names=F, col.names=F)
