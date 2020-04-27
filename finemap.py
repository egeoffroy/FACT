# This script is the new main wrapper once the COLOC features are added to the overall pipeline

import os
import sys
import argparse 
import shlex
import subprocess
import logging
from os import path

logger = logging.getLogger(__name__)
logFormatter = '%(message)s'
logging.basicConfig(filename='FACT_logger.log', format=logFormatter, level=logging.DEBUG)

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Run fastenloc or coloc for various GWAS SS')
    parser.add_argument('--coloc',action="store_true", dest="coloc", default=False,
                        help='input test type'
                        )
    parser.add_argument('-fastenloc', '--fastenloc', action="store_true", dest="fastenloc", default=False,
                        help='input test type'
                        )
    parser.add_argument('-fastenloc_SS', '--fastenloc_SS', action="store_true", dest="fastenloc_SS", default=False,
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
    parser.add_argument('-m', '--genemap',
                        help='gene position map'
                        )
    parser.add_argument('-LD', '--LD',
                        help='LD blocks locus file'
                        )
    parser.add_argument('-chr', '--chr',
                        help='chromosome range', default=[1, 22], nargs='+'
                        )
    parser.add_argument('-pop_size', '--pop_size',
                        help='Population size'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])

if args.coloc:
    logging.info("Running COLOC pipeline.")
    os.chdir('./coloc')
    if os.path.isdir('./summary-gwas-imputation') == FALSE: #path.exists('summary-gwas-imputation'):
        os.system('git clone https://github.com/hakyimlab/summary-gwas-imputation.git')
    if args.meqtl: 
            os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --meqtl ' + args.meqtl + ' --pop_size ' + args.pop_size)
            if args.filter_by:
                os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by + ' --meqtl ' + args.meqtl + ' --pop_size ' + args.pop_size)
    if args.filter_by:
            os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --filter_by ' + args.filter_by + ' --pop_size ' + args.pop_size)
    os.system('python3 coloc_pipeline_main.py --pop ' + args.pop + ' --gwas_SS ' + args.gwas_SS + ' --frq ' + args.frq + ' --pheno_id ' + args.pheno_id + ' --pop_size ' + args.pop_size)

if args.fastenloc: # Updated: works
    os.chdir('./db2fastenloc')
    logging.info("Running FASTENLOC pipeline.")
    if args.chr:
         start = args.chr[0]
         stop = args.chr[1]
         make_cmd = 'python3 main.py --geno {} --meqtl {} --genemap {} --pop {} --gwas_SS {} --LD_block {} --start {} --stop {} --gwas_out_prefixes {}'.format(args.geno, args.meqtl, args.genemap, args.pop, args.gwas_SS, args.LD, start, stop, args.pheno_id)
         os.system(make_cmd)
         chr_info = 'Chromosomes tested are {} through {}'.format(start,stop)
         logging.info(chr_info)
    else:
        print('No chromosome entered. Using default chromosomes 1 through 22')
        logging.info("No chromosome user input. Testing chromosomes 1 through 22.")

if args.fastenloc_SS:
    logging.info("Running FASTENLOC test pipeline")
    os.chdir('./db2fastenloc')
    make_cmd = 'python3 main.py --pop {} --gwas_SS {} --LD_block {} --gwas_out_prefixes {}'.format(args.pop, args.gwas_SS, args.LD, args.pheno_id)
    os.system(make_cmd)
    
else:
    print('No input test type selected.')
    logging.info("No input test type selected.")
