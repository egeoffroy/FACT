# FACT+ : Fine-mapping and Colocalization Pipeline

## Languages and Packages
#### - Bash
#### - Python3
                - os
                - subprocess
                - shlex
                - argparse
                - logging
                - sys

#### - R 
                - dplyr
                - data.table
                - coloc
                - R.utils
                
## Software Required:
#### - DAP-G: https://github.com/xqwen/dap
#### - TORUS: https://github.com/xqwen/torus
#### - FASTENLOC: https://github.com/xqwen/fastenloc
#### - Summary GWAS Imputation: https://github.com/hakyimlab/summary-gwas-imputation/

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

### Summary GWAS Imputation

```
git clone https://github.com/hakyimlab/summary-gwas-imputation.git
```
Clone this into the [coloc](https://github.com/egeoffroy/Fine-mapping_Pipeline/tree/master/coloc) directory. 

## Tutorial:
Please see the [wiki](https://github.com/egeoffroy/Fine-mapping_Pipeline/wiki). 




## References:
1. International HapMap Consotorium. The International HapMap Project. Nature. 2003;426(6968):789-796.
2. Wojcik, G.L., Graff, M., Nishimura, K.K. et al. Genetic analyses of diverse populations improves discovery for complex traits. Nature. 2019;570:514–518. 
3.	Wen, X., Lee, Y., Luca, F., Pique-Regi, R. Efficient integrative multi-SNP association analysis using Deterministic Approximation of Posteriors. The American Journal of Human Genetics. 2016 May 26;98(6):1114-1129. 
4.	Wen X, Pique-Regi R, Luca F. Integrating molecular QTL data into genome-wide genetic association analysis: Probabilistic assessment of enrichment and colocalization. PLoS Genet. 2017;13(3):e1006646. 
5.	Wen, Xiaoquan. Molecular QTL discovery incorporating genomic annotations using Bayesian false discovery rate control. Ann. Appl. Stat. 10. 2016;no. 3:1619-1638. 
6. Giambartolomei C, Vukcevic D, Schadt EE, Franke L, Hingorani AD, Wallace C, et al. Bayesian test for colocalisation between pairs of genetic association studies using summary statistics. PLoS Genet. 2014;10(5):e1004383. 

