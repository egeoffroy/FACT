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
    parser.add_argument('-dat', '--out_dat_dir',
                        help='output .dat file directory',
                        required='True'
                        )
    parser.add_argument('-gwas', '--gwas_SS',
                        help='GWAS Summary Statistics File',
                        required='True'
                        )
    parser.add_argument('-LD', '--LD',
                        help='LD blocks locus file',
                        required='True'
                        )
    parser.add_argument('-gwas_out_prefix', '--gwas_out_prefix',
                        help='prefix for GWAS Summary Statistics reformatted file',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
geno_folder = args.geno
phenofile = args.pheno
genemapfile = args.genemap
outdir = args.dat
pop = args.pop
gwasSS = args.gwas_SS
LD = args.LD
gwas_prefix = args.gwas_out_prefix

os.system('mkdir ' + pop + '_all1Mb_sbams')
os.system('python3 run_scripts/make_run_scripts_01.py --geno '+geno_folder+' --pheno '+phenofile+' --genemap '+genemapfile+' --pop '+pop+' --outdir' + pop + '_sbams/')
os.system('bash qsub_01.txt')
os.system('python3 02_all1MbSNPs_batch_scan.py --pop ' + pop)
os.system('nohup run_scripts/run_02_all1MbSNPs_batch_scan.sh ' + pop)
os.system('python3 02b_concat_scan_out_bf_files.py --pop ' + pop)
os.system('bash 03_all1MbSNPs_torus.sh ' + geno_folder + ' ' + genemapfile + ' ' + pop)
os.system('python3 04_all1MbSNPs_batch_dapg.py --pop ' + pop)
os.system('python3 05_make_vcf.py --geno ' + geno_folder + ' --pop' + pop)
os.system('bash 06_all1MbSNPs_make_fastenloc_anot.sh ' + pop) #Run script 06
os.system('python3 07_prep_sumstats_1000G_LDblocks.py --ldblocks ' + LD + '--s ' + gwasSS + ' --annot ' +pop + '_all1Mb_fastenloc.eqtl.annotation.vcf.gz' + ' --outprefix ' + gwas_prefix)
os.system('bash 08_gwas_zval_torus.sh ' + gwas_prefix)
os.system('bash 09_all1MbSNPs_fastenloc.sh ' + gwas_prefix + ' ' + pop)


