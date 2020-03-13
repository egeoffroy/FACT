import os
import sys
import argparse
#Example Files --will be added to CompBio server over weekend
#pop = YRI
#outdir for 01 = pop + 'sbams/'
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Matrix EQTL to .dat format from .db SNP list')
    parser.add_argument('-g', '--geno',
                        help='input genotype folder',
                        required='True'
                        )
    parser.add_argument('-p', '--pheno',
                        help='input phenotype file',
                        required='True'
                        )
    parser.add_argument('-m', '--genemap',
                        help='gene position map',
                        required='True'
                        )
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    parser.add_argument('-o', '--outdir',
                        help='output .dat file directory',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
geno_folder = args.geno
phenofile = args.pheno
genemapfile = args.genemap
outdir = args.outdir
pop = args.pop

os.system('python3 run_scripts/make_run_scripts_01.py --geno '+geno_folder+' --pheno '+phenofile+' --genemap '+genemapfile+' --pop '+pop+' --outdir' + pop + '_sbams/')
os.system('bash qsub_01.txt')
os.system('python3 02_all1MbSNPs_batch_scan.py --pop ' + pop)
os.system('python3 02b_concat_scan_out_bf_files.py --pop ' + pop)
os.system('bash 03_all1MbSNPs_torus.sh' + geno_folder + ' ' + genemapfile + ' ' + pop)
os.system('python3 04_all1MbSNPs_batch_dapg.py --pop ' + pop)



