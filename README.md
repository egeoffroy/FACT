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

GNU GSL library
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
#### Gene Expression Prediction matrix eQTL file
#### Linkage Disequilibrium annotation file 
#### Gene Annotation file
#### GWAS Summary Statistics file
#### n: the number of individuals in the model

## Output:
1. Enrichment analysis result: estimated enrichment parameters and standard errors.
2. Signal-level colocalization result: the main output from the colocalization analysis with the following columns
signal cluster name (from eQTL analysis), number of member SNPs, cluster PIP of eQTLs, cluster PIP of GWAS hits (without eQTL prior), cluster PIP of GWAS hits (with eQTL prior), regional colocalization probability (RCP)
3. SNP-level colocalization result: SNP-level colocalization output with the following columns
signal cluster name, SNP name, SNP-level PIP of eQTLs, SNP-level PIP of GWAS (without eQTL prior), SNP-level PIP of GWAS (with eQTL prior), SNP-level colocalization probability
4. A sorted list of colocalization signals
5. Potentially some figures to analyze the output 

