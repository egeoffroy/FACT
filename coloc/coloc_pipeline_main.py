import os
import sys
import argparse
import subprocess
import os.path
from os import path
def check_arg(args=None): #get arguments for COLOC
    parser = argparse.ArgumentParser(description='Run coloc for various GWAS SS')
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
    parser.add_argument('-pop_size', '--pop_size',
                        help='Population size'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
phenoid = args.pheno_id #assign arguments to variables
pop = args.pop
frqfile = args.frq
gwasSS = args.gwas_SS
pop_size = args.pop_size


if path.isdir('coloc'):
        print('Directory coloc exists') 
else:
        os.system('mkdir coloc') #make output directory if not already existing

command = 'Rscript SNP_list.R ' + gwasSS + ' ' + phenoid #get SNP list
result = subprocess.getoutput(command)

#make coloc input files --> format eQTL and GWAS data
if args.meqtl: #if user inputs meqtl file
    os.system('Rscript make_coloc_files.R ' + gwasSS + ' ' + frqfile + ' ' + phenoid + ' ' + pop + ' ' + pop_size + ' ' + args.meqtl) 
else:
    os.system('Rscript make_coloc_files.R ' + gwasSS + ' ' + frqfile + ' ' + phenoid + ' ' + pop + ' ' + pop_size) 
os.system('bash run_pipeline_1.sh ' + pop + ' ' + phenoid + ' ' + pop_size) #run COLOC

if args.filter_by: #filter results in user includes filtering PrediXcan significant genes file
    os.system('Rscript filter_results.R ' + phenoid + ' ' + pop + ' ' + args.filter_by)
