# Sample Data For Tutorial

## Test FASTENLOC Pipeline

```
cd Fine-mapping_Pipeline
mv YRI_all1Mb_fastenloc.eqtl.annotation.vcf.gz ./db2fastenloc
python3 finemap.py --fastenloc_SS --pop YRI --LD sample_data/AFR_fourier_ls-all.bed --gwas_SS sample_data/312..... --pheno_id Wojcik_Height

```

## Test COLOC Pipeline
```
cd Fine-mapping_Pipeline
python3 finemap.py --coloc --pop YRI ---pop_size 107 --meqtl sample_data/YRI_meqtl_input.txt --frq sample_data/YRI_plink.frq --gwas_SS sample_data/312..... --pheno_id Wojcik_Height

```
