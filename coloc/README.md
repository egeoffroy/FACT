# COLOC: Colocalisation Tests of Two Genetic Traits
COLOC (Colocalisation Tests of Two Genetic Traits) is a fine-mapping technique that is published as an R package in the CRAN. It was published before fine-mapping GWAS and TWAS results was standardized; however, it is still commonly used. COLOC looks at a single genomic region at a time with a major focus on interpreting LD patterns at that particular loci; however, it assumes that there is only one causal SNP. This method uses an Approximate Bayes Factor Model approach to colocalization and fits each variant to a linear regression model. The requirements to run COLOC are minimal in that it only needs the SNP id and p-value, although including the regression coefficient, variances, and standard error are preferred. 


However, COLOC does not account for certain biological circumstances. Since it assumes only causal SNP and/or one qualitative trait nucleotide within the locus of interest, it fails to accurately identify when there are multiple causal SNPs like other colocalization and fine-mapping tools. COLOC also predefines the initial prior probability (probability of an event before new data is taken into consideration), making it less precise unless the priors are known beforehand. It lacks the statistical rigor of more recent tools. While this tool may not be the most sophisticated, it is well documented and offers clear explanations and instructions. It claims to be computational quick as it does not use a Markov Chain Monte Carlo approach.

## Software:
R Libraries
* coloc
* dplyr
* data.table
* R.utils


Python Libraries
* os
* subprocess
* argparse
* os.path

Clone [this](https://github.com/hakyimlab/summary-gwas-imputation) GitHub repository into this directory. 


## Input:
--pheno_id: Phenotype ID

--pop: Population ID

--gwas_SS: GWAS Summary Statistics

--meqtl: meQTL file

--frq: .frq file from PLINK

--filter_by: an optional flag signaling the script to also run the script filter_results.R with the inputted file of significant genes from S-PrediXcan or PrediXcan.

## Run Software:

### Script Description
SNP_list.R: pull out the SNPs from the GWAS Summary Statistics that were found to be associated with the particular trait. Only run COLOC on these SNPs, not all the SNPs in the eQTL file.

make_coloc_files.R: comverts eQTL and GWAS into the proper COLOC input format. Requires the matrix eQTL file, significant SNPs file, GWAS and eQTL sizes, frq file, and GWAS Summary Statistics file.

filter_results.R: an optional script to filter out the genes that were found to be significant in PrediXcan/S-PrediXcan. Requires the user to use the flag --filter_by. This file must contain a column called GENE.

coloc_pipeline_main.py: main wrapper file for the pipeline.

### Run the Program
```
python3 coloc_pipeline_main.py --pheno_id ${pheno} --pop ${pop} --gwas_SS ${gwas} --frq ${frq} --meqtl ${meqtl} --filter_by ${PrediXcan significant hits file}
```


## Output: 
COLOC returns five posterior probabilities (PP) for each of the two SNPs tested. If the third posterior probability (PP3) is large, then they conclude there are two independent causal SNPs associated with each trait. If the PP4 is large, then only a single variant is affecting both traits. If PP0 is large, neither SNP is in association with the trait. 

#### P0: There is no SNP or variant that has association with either trait 1 or trait 2
#### P1: One SNP/variant has association with trait 1 but not with trait 2
#### P2: One SNP/variant has association with trait 2 but not with trait 1
#### P3: Two independent causal SNPs/variants associated with each trait
#### P4: One single SNP/variant associated with each trait

