library(dplyr)
library(data.table)
library(R.utils)

args = commandArgs(trailingOnly=TRUE)
prefix = args[1]
pop = args[2]
data <- fread(paste(prefix, ".enloc.sig.out", sep = ''), header =F)
print(head(data))
data <- data %>% filter(V6 >= 0.5)
write.table(data, paste(prefix, "significant_rcp.txt", sep=''), quote=F, col.names=F, row.names=F)
