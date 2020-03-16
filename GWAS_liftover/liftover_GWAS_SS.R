library(dplyr)
library(tidyr)
library(data.table)
library(argparse)

parser <- ArgumentParser()
parser$add_argument("--gwas", help="GWAS Summary Statistic file")
parser$add_argument("-o","--out", help="Output file path")
args <- parser$parse_args()
"%&%" = function(a,b) paste (a,b,sep="")
lifted_coordinates<-fread("~/liftover/lifted.hg38")
GWAS<-fread(args$gwas)
colnames(lifted_coordinates)<-c("chrom","hg38_pos","pos2","rsid")
lifted_coordinates<- lifted_coordinates %>% mutate(SNP_hg38=paste(chrom,hg38_pos,sep=":"))

joined<-inner_join(lifted_coordinates,GWAS,by="rsid") %>% select(-Chr,-Position_hg19,-SNP,-pos2)
#colnames(joined)

fwrite(joined, args$out,sep='\t')
