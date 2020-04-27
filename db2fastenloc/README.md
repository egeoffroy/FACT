# FASTENLOC 

## Tutorial:
Please see [wiki](https://github.com/egeoffroy/Fine-mapping_Pipeline/wiki).

____________________________________________________________________________________________________________________________________
## FASTENLOC Input: 
* --geno : Folder path to genotype and genotype annotation data
* --LD_block : Linkage Disequilibrium annotation file 
* --genemap : Gene Annotation file
* --gwas_SS : gzipped, harmonised GWAS Summary Statistics file
* --meqtl : Matrix eQTL gene expression file
* --pop : population id
* --gwas_out_prefixes : prefixes for GWAS phenotypes
* --chr : a range of chromosome numbers. The default is chromsomes 21 and 22. 
* --start : start chromosome [optional]
* --stop : end chromosome [optional]

## FASTENLOC Scripts
1. Convert mEQTL file to .dat files → file for every gene
2. Run DAP-G with each dat file
3. Run TORUS with eQTL data
4. Run DAP-G with eQTL data
5. Make .vcf file
6. Make fastenloc annotation file for eQTL data.
7. Identify important columns in GWAS Summary Statistics file. Transform GWAS SS file to include z-scores and label LD blocks using LD annotation file and fastenloc annotation file.
8. Run torus with GWAS SS data
9. Run fastenloc with GWAS SS data
10. Identify top 10 genes based on RCP value.


## FASTENLOC Output:
1. Enrichment analysis result: estimated enrichment parameters and standard errors.
2. Signal-level colocalization result: the main output from the colocalization analysis with the following columns
signal cluster name (from eQTL analysis), number of member SNPs, cluster PIP of eQTLs, cluster PIP of GWAS hits (without eQTL prior), cluster PIP of GWAS hits (with eQTL prior), regional colocalization probability (RCP)
3. SNP-level colocalization result: SNP-level colocalization output with the following columns
signal cluster name, SNP name, SNP-level PIP of eQTLs, SNP-level PIP of GWAS (without eQTL prior), SNP-level PIP of GWAS (with eQTL prior), SNP-level colocalization probability
4. A sorted list of colocalization signals
5. Potentially some figures to analyze the output 
6. Log file that displays pipeline steps.
