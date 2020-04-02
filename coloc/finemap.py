# This script is the new main wrapper once the COLOC features are added to the overall pipeline

import os
import sys
import subprocess
import argparse 

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Run fastenloc or coloc for various GWAS SS')
    parser.add_argument('-coloc', '--coloc',
                        help='input test type'
                        )
    parser.add_argument('-fastenloc', '--fastenloc',
                        help='input test type'
                        )
    parser.add_argument('-pid', '--pheno_id',
                        help='input phenotype id',
                        required='True'
                        )
    parser.add_argument('-b', '--pop',
                        help='population',
                        required='True'
                        )
    parser.add_argument('-gwas', '--gwas_SS',
                        help='GWAS Summary Statistics File',
                        required='True'
                        )
    parser.add_argument('-meqtl', '--meqtl',
                        help='meQTL file'
                        )
    parser.add_argument('-frq', '--frq',
                        help='.frq file',
                        required='True'
                        )
    parser.add_argument('-filter_by', '--filter_by',
                        help='filter by this file of significant genes from S-PrediXcan/PrediXcan output. Requires gene column'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])

if args.coloc:
    if args.meqtl: 
            os.system('python3 ./coloc/coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --meqtl ' + args.meqtl)
            if args.filter_by:
                os.system('python3 ./coloc/coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by + ' --meqtl ' + args.meqtl)
    if args.filter_by:
            os.system('python3 ./coloc/coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by)
    os.system('python3 ./coloc/coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id)

#if args.fastenloc: 
#os.system('python3 main.py --geno ' + genotype_folder + ' --pheno ' + meqtl_file + ' --genemap ' + genemap_file + ' --pop ' + population_id+ ' --gwas_SS ' + GWAS_SS_file +' --LD ' + LD_annotation_file+' --gwas_out_prefixes '+ GWAS_Prefix)
