# COLOC: Colocalisation Tests of Two Genetic Traits
COLOC (Colocalisation Tests of Two Genetic Traits) is a fine-mapping technique that is published as an R package in the CRAN. It was published before fine-mapping GWAS and TWAS results was standardized; however, it is still commonly used. COLOC looks at a single genomic region at a time with a major focus on interpreting LD patterns at that particular loci; however, it assumes that there is only one causal SNP. This method uses an Approximate Bayes Factor Model approach to colocalization and fits each variant to a linear regression model. The requirements to run COLOC are minimal in that it only needs the SNP id and p-value, although including the regression coefficient, variances, and standard error are preferred. 


However, COLOC does not account for certain biological circumstances. Since it assumes only causal SNP and/or one qualitative trait nucleotide within the locus of interest, it fails to accurately identify when there are multiple causal SNPs like other colocalization and fine-mapping tools. COLOC also predefines the initial prior probability (probability of an event before new data is taken into consideration), making it less precise unless the priors are known beforehand. It lacks the statistical rigor of more recent tools. While this tool may not be the most sophisticated, it is well documented and offers clear explanations and instructions. It claims to be computational quick as it does not use a Markov Chain Monte Carlo approach.

## Software:
R Libraries
* coloc
* dplyr
* data.table

Python Libraries
* os
* subprocess
* argparse

Clone [this](https://github.com/hakyimlab/summary-gwas-imputation) GitHub repository into this directory. 


## Input:
--pheno_id: Phenotype ID
--pop: Population ID
--gwas_SS: GWAS Summary Statistics
--meqtl: meQTL file
--frq: .frq file from PLINK



## Output: 
COLOC returns five posterior probabilities (PP) for each of the two SNPs tested. If the third posterior probability (PP3) is large, then they conclude there are two independent causal SNPs associated with each trait. If the PP4 is large, then only a single variant is affecting both traits. If PP0 is large, neither SNP is in association with the trait. 

#### P0: There is no SNP or variant that has association with either trait 1 or trait 2
#### P1: One SNP/variant has association with trait 1 but not with trait 2
#### P2: One SNP/variant has association with trait 2 but not with trait 1
#### P3: Two independent causal SNPs/variants associated with each trait
#### P4: One single SNP/variant associated with each trait

