# This script is the new main wrapper once the COLOC features are added to the overall pipeline

import os
import sys
import subprocess
import argparse 

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Run fastenloc or coloc for various GWAS SS')
    parser.add_argument('--coloc',action="store_true", dest="coloc", default=False,
                        help='input test type'
                        )
    parser.add_argument('-fastenloc', '--fastenloc', action="store_true", dest="fastenloc", default=False,
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
                        help='.frq file'
                        )
    parser.add_argument('-filter_by', '--filter_by',
                        help='filter by this file of significant genes from S-PrediXcan/PrediXcan output. Requires gene column'
                        )
    parser.add_argument('-g', '--geno',
                        help='input genotype folder'
                        )
    parser.add_argument('-p', '--pheno',
                        help='input phenotype file'
                        )
    parser.add_argument('-m', '--genemap',
                        help='gene position map'
                        )
    parser.add_argument('-LD', '--LD',
                        help='LD blocks locus file'
                        )
    parser.add_argument('-gwas_out_prefixes', '--gwas_out_prefixes',
                        help='prefixes for GWAS Summary Statistics reformatted file'
                        )
    parser.add_argument('-chr', '--chr',
                        help='chromosome range', default=[22, 23],
                        required='False'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])

if args.coloc:
    os.chdir('./coloc')
    if args.meqtl: 
            os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --meqtl ' + args.meqtl)
            if args.filter_by:
                os.system('python3 .coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by + ' --meqtl ' + args.meqtl)
    if args.filter_by:
            os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by)
    os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id)

if args.fastenloc: 
    os.system('cd db2fastenloc/')
    os.system('python3 main.py --geno ' + args.geno + ' --pheno ' + args.pheno + ' --genemap ' + args.genemap + ' --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS +' --LD ' + args.LD +' --chr ' + args.chr + ' --gwas_out_prefixes '+ args.gwas_out_prefixes)
