## GWAS Summary Statistics 

### Use these scripts if you need to change the build of the GWAS Summary Statistics from hg19 to hg38.

### Scripts:
#### liftover_GWAS_SS.R : R script to transform the GWAS Summary Statistics data from genome build hg19 to hg38. 
**Parameters:**

      - GWAS : GWAS Summary Statistics File
      - out : output file path
#### run_liftover.sh : bash script that runs liftover_GWAS_SS.R with appropriate user-specified parameters. 


### Tutorial

#### Input:
GWAS : WojcikG_PMID_lnwbc.out.gz. This file can be found here: ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/WojcikGL_31217584_GCST008049/WojcikG_PMID_lnwbc.out.gz

Out : WojcikG_hg38_WBC.out

#### Process:

```
bash run_liftover.sh WojcikG_PMID_lnwbc.out.gz WojcikG_hg38_WBC.out
```

The first user-specified parameter should be the input file path while the second parameter should be the output file name. 

#### Output: 
| chrom | hg38_pos | rsid | SNP_hg38 | Other-allele |  Effect-allele | Effect-allele-frequency | Sample-size | Beta | SE | P-val | INFO-score |
_________________________________________________________________________________________________________________________________
chr1    10539   rs537182016     chr1:10539      C       A       0.005526652     28534   -0.01723274     0.02457384      0.4831384       0.46
_________________________________________________________________________________________________________________________________
chr1    10616   rs376342519     chr1:10616      CCGCCGTTGCAAAGGCGCGCCG  C       0.994645        28534   0.01135124      0.02302719      0.6220484       0.604
__________________________________________________________________________________________________________________________________
chr1    10642   rs558604819     chr1:10642      G       A       0.005460416     28534   0.01093552      0.02604575      0.6745892       0.441
__________________________________________________________________________________________________________________________________
chr1    11008   rs575272151     chr1:11008      C       G       0.1082466       28534   0.007125214     0.005505301     0.1955804       0.5
__________________________________________________________________________________________________________________________________
chr1    11012   rs544419019     chr1:11012      C       G       0.1082466       28534   0.007125214     0.005505301     0.1955804       0.5
