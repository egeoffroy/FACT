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

____________________________________________________________________________________________________________________________________

## COLOC Input:
* --gwas_SS : a gzipped, harmonised GWAS Summary Statistics file
* --frq : .frq PLINK file
* --meqtl : Matrix eQTL Gene expression file (optional)
* --filter_by: an optional flag signaling the script to also run the script filter_results.R with the inputted file of significant genes from S-PrediXcan or PrediXcan.
* --pop : population id
* --pop_size : eQTL population size
* --pheno_id : phenotype id

## COLOC Scripts:
1. SNP_lists.R : script that takes all of the GWAS Summary Statistics SNPs and writes them out to a separate file to only use those SNPs later.
2. make_coloc_files.R : formats Matrix eQTL and GWAS Summary Statistics data into the proper COLOC input. Also requires the output from SNP_lists.R and the .frq file.
3. coloc_pipeline_main.py : main pipeline wrapper that ties together the other scripts. 
4. run_pipeline_1.sh: calls the [pipeline](https://github.com/hakyimlab/summary-gwas-imputation) developed by the Im Lab at UChicago to run COLOC with the properly formatted files.

## COLOC Output:
1. output_pop_pheno.txt.gz: COLOC output. A file with the probabilites for each of the five hypotheses for each gene.
2. sig_genes_coloc_pop_pheno.csv: The filtered COLOC output file by only looking at the genes found significant by the TWAS Method.


This program works for six different populations--the five MESA populations and the International HapMap Project's Yoruban population.
* ALL
* AFHI
* AFA
* HIS
* CAU
* YRI


*It is required that the GWAS Summary Statistics are the new harmonised versions as these only include the SNPs found to be significant in the original study and have standard column names. The GWAS Summary Statistics must also be gzipped.

## Run COLOC:
To run the COLOC Pipeline in FACT+:
```
python3 finemap.py --pheno_id ${pheno} --pop ${pop} --gwas_SS ${gwas} --frq ${frq} --meqtl ${meqtl} --filter_by ${PrediXcan significant hits file}

```

## Run COLOC Pipeline Separately:
To run the COLOC Pipeline outside of the FACT+:

```
python3 coloc_pipeline_main.py --pheno_id ${pheno} --pop ${pop} --gwas_SS ${gwas} --frq ${frq} --meqtl ${meqtl} --filter_by ${PrediXcan significant hits file}

```


## Output Description: 
COLOC returns five posterior probabilities (PP) for each of the two SNPs tested. If the third posterior probability (PP3) is large, then they conclude there are two independent causal SNPs associated with each trait. If the PP4 is large, then only a single variant is affecting both traits. If PP0 is large, neither SNP is in association with the trait. 

#### P0: There is no SNP or variant that has association with either trait 1 or trait 2
#### P1: One SNP/variant has association with trait 1 but not with trait 2
#### P2: One SNP/variant has association with trait 2 but not with trait 1
#### P3: Two independent causal SNPs/variants associated with each trait --> non-colocalized GWAS and eQTL signals
#### P4: One single SNP/variant associated with each trait --> colocalized GWAS and eQTL signals

