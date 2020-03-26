# Fine-mapping Pipeline

## Languages and Packages
#### - Bash
#### - Python3
                - os
                - subprocess
                - shlex
                - argparse

#### - R 
                - dplyr
                - data.table
                
## Software Required:
#### - DAP-G: https://github.com/xqwen/dap
#### - TORUS: https://github.com/xqwen/torus
#### - FASTENLOC: https://github.com/xqwen/fastenloc

## Install Software

### DAP-G 
The following C/C++ libraries are required for compiling the source code

GNU [GSL](https://www.gnu.org/software/gsl/) library
OpenMP compiler (many popular compilers are compatible)

Simply run ```make``` to compile the executable named ```dap```.

Run ```make static``` to compile an executable with static linked library.
```
git clone https://github.com/xqwen/dap.git
cd dap/dap_src
make
```

### TORUS


```
git clone https://github.com/xqwen/torus.git
cd torus/src
make
```

### FASTENLOC 

```
git clone https://github.com/xqwen/fastenloc.git
cd fastenloc/src
make
```


## Tutorial:
Please see the [wiki](https://github.com/egeoffroy/Fine-mapping_Pipeline/wiki). 

## Input: 
* --geno : Gene Expression Prediction matrix eQTL folder
* --LD : Linkage Disequilibrium annotation file 
* --genemap : Gene Annotation file
* --gwas_SS : GWAS Summary Statistics file
* --gwas_n : n: the number of individuals in the model

## Scripts
1. Convert mEQTL file to .dat files → file for every gene
2. Run DAP-G with each dat file
3. Run TORUS with eQTL data
4. Run DAP-G with eQTL data
5. Make .vcf file
6. Make fastenloc annotation file for eQTL data.
7. Identify important columns in GWAS Summary Statistics file. Transform GWAS SS file to include z-scores and label LD blocks using LD annotation file and fastenloc annotation file.
8. Run torus with GWAS SS data
9. Run fastenloc with GWAS SS data
10. Identify significant genes with RCP > 0.5


## Output:
1. Enrichment analysis result: estimated enrichment parameters and standard errors.
2. Signal-level colocalization result: the main output from the colocalization analysis with the following columns
signal cluster name (from eQTL analysis), number of member SNPs, cluster PIP of eQTLs, cluster PIP of GWAS hits (without eQTL prior), cluster PIP of GWAS hits (with eQTL prior), regional colocalization probability (RCP)
3. SNP-level colocalization result: SNP-level colocalization output with the following columns
signal cluster name, SNP name, SNP-level PIP of eQTLs, SNP-level PIP of GWAS (without eQTL prior), SNP-level PIP of GWAS (with eQTL prior), SNP-level colocalization probability
4. A sorted list of colocalization signals
5. Potentially some figures to analyze the output 
6. Log file that displays pipeline steps.

## References:
1. International HapMap Consotorium. The International HapMap Project. Nature. 2003;426(6968):789-796.
2. Wojcik, G.L., Graff, M., Nishimura, K.K. et al. Genetic analyses of diverse populations improves discovery for complex traits. Nature. 2019;570:514–518. 
3.	Wen, X., Lee, Y., Luca, F., Pique-Regi, R. Efficient integrative multi-SNP association analysis using Deterministic Approximation of Posteriors. The American Journal of Human Genetics. 2016 May 26;98(6):1114-1129. 
4.	Wen X, Pique-Regi R, Luca F. Integrating molecular QTL data into genome-wide genetic association analysis: Probabilistic assessment of enrichment and colocalization. PLoS Genet. 2017;13(3):e1006646. 
5.	Wen, Xiaoquan. Molecular QTL discovery incorporating genomic annotations using Bayesian false discovery rate control. Ann. Appl. Stat. 10. 2016;no. 3:1619-1638. 

