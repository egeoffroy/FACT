import os
import sys
import argparse
import shlex
import subprocess
import logging

logger = logging.getLogger(__name__)
logFormatter = '%(message)s'
logging.basicConfig(filename='ProgressLogger.log', format=logFormatter, level=logging.DEBUG)

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Matrix EQTL to .dat format from .db SNP list')
    parser.add_argument('-g', '--geno',
                        help='input genotype folder'
                        )
    parser.add_argument('-meqtl', '--meqtl',
                        help='input meqtl file'
                        )
    parser.add_argument('-m', '--genemap',
                        help='gene position map'
                        )
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
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
    parser.add_argument('-gwas_out_prefixes', '--gwas_out_prefixes',
                        help='prefixes for GWAS Summary Statistics reformatted file',
                        required='True'
                        )
    parser.add_argument('-chr', '--chr',
                        help='chromosome range', nargs='+', default=[21, 22],
                        required='False'
                        )
    parser.add_argument('-start', '--start',
                        help='chromosome range start',  default=21
                        )
    parser.add_argument('-stop', '--stop',
                        help='chromosome range stop', default=22
                        )
    return parser.parse_args(args)

#retrieve command line arguments
logging.info("Beginning db2fastenloc pipeline")
args = check_arg(sys.argv[1:])
pop = args.pop
gwasSS = args.gwas_SS
LD = args.LD
gwas_prefix = args.gwas_out_prefixes
if args.chr:
    log_a = 'Chromosomes tested are: {} {}'.format(args.chr[0], args.chr[1])
    logging.info(log_a)
    start = args.chr[0]
    stop = args.chr[1]
else:
    log_b = 'Chromosomes tested are: {} {}'.format(start, stop)
    logging.info(log_b)
    start = args.start
    stop = args.stop
    
if args.geno :
    geno_folder = args.geno
    phenofile = args.meqtl
    genemapfile = args.genemap
    logging.info("Making directory for all 1Mb sbams")
    os.system('mkdir ' + pop + '_all1Mb_sbams')
    logging.info("Make Run Scripts")
    os.system('python3 run_scripts/make_run_scripts_01.py --geno '+geno_folder+' --meqtl '+phenofile+' --genemap '+genemapfile+' --pop '+pop+' --outdir ' + pop + '_all1Mb_sbams --start ' + start + ' --stop ' + stop)
    #work on timing between steps to prevent the program from going over steps before files are ready
    os.system('bash nohup_01.txt')
    #os.system('at now + 7 hours')
    os.system('bash run_scripts/run_02_all1MbSNPs_batch_scan.sh ' + pop)
    os.system('python3 02b_concat_scan_out_bf_files.py --pop ' + pop)
    logging.info('Running TORUS')
    os.system('bash 03_all1MbSNPs_torus.sh ' + geno_folder + ' ' + genemapfile + ' ' + pop)
    os.system('bash run_scripts/run_04_all1MbSNPs_batch_dapg.sh ' + pop)
    os.system('bash run_scripts/run_05_make_vcf.py  '+ geno_folder + ' ' + pop)
    logging.info('Making fastenloc annotation files')
    os.system('bash 06_all1MbSNPs_make_fastenloc_anot.sh ' + pop) 

if gwasSS: 
        logging.info('Running summary stats')
        os.system('Rscript 07a_sumstats_names.R ' + gwasSS)
        os.system('python3 07_prep_sumstats_1000G_LDblocks.py --ldblocks ' + LD + ' --sumstats ' + gwasSS + ' --pop ' + pop + ' --annot ' + pop + '_all1Mb_fastenloc.eqtl.annotation.vcf.gz' + ' --outprefix ' + gwas_prefix)
        logging.info('Running TORUS on gwas SS')
        os.system('bash 08_gwas_zval_torus.sh ' + gwas_prefix + ' ' + pop)
        logging.info('Running fastenloc')
        os.system('bash 09_all1MbSNPs_fastenloc.sh ' + gwas_prefix + ' ' + pop)
        logging.info('Getting significant RCP values')
        os.system('Rscript 10_get_sig_RCP.R ' + gwas_prefix + ' ' + pop)
        


