#assign LD block loci to snps
library(data.table)
library(dplyr)
library(argparse)
library(tidyr)

parser <- ArgumentParser()
parser$add_argument("--assoc", help="path to GWAS")
parser$add_argument("--LD", help="full path to the annotation file")
parser$add_argument("-o", "--out", help="As in plink prefix optionally including PATH")
args <- parser$parse_args()
"%&%" = function(a,b) paste (a,b,sep="")
#

assoc<-fread(args$assoc,header = T,showProgress = T)
LD<-fread(args$LD)


lower<-c(0,unlist(LD[,2]))
test<-assoc
str(lower)
assoc<-assoc %>%
  mutate(zscore=Beta/SE) %>%
  #mutate(chr=paste("chr",chr,sep="")) %>%
  #mutate(cpos=paste(achr,":",ps,sep="")) %>%
  select(chrom,SNP_hg38,hg38_pos,zscore) %>%
  mutate(bin=cut(x=assoc$hg38_pos, breaks = lower,include.lowest = T)) %>%
  mutate(bin=gsub("\\(|\\]","",bin)) %>%
  mutate(bin=gsub(",",":",bin)) %>%
  mutate(bin=paste(chrom,bin,sep=":"))


assoc<-assoc %>% select(SNP_hg38,bin,zscore)
str(assoc)
fwrite(assoc,args$out,sep='\t',col.names = F)
