import os
import shlex
import subprocess
import logging
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
    parser.add_argument('-n', '--gwas_n', default=1,
                        help='Number of GWAS Summary Statistics Files With Same Format',
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
    #check this with Elyse
    #need to determine where to place if statement
    parser.add_argument('-chr','--chr',
                        help='Chromosome number (range) being tested in pipeline',
                        required='False'
                        )
    return parser.parse_args(args)

def main():
#retrieve command line arguments\
    logging.info("Beginning to run wrapper.")
    args = check_arg(sys.argv[1:])
    geno_folder = args.geno
    phenofile = args.pheno
    genemapfile = args.genemap
    outdir = args.out_dat_dir
    pop = args.pop
    gwas_n = args.gwas_n #This may not be needed
    gwasSS = args.gwas_SS
    LD = args.LD
    gwas_prefix = args.gwas_out_prefixes
    ch_chr = args.chr
    chosen_chr = "Chromosome range being tested in pipeline is {}".format(ch_chr)
    logging.info(chosen_chr)
    
    if args.geno:
        
        logging.info("Making directory")
        mkdir_cmd = 'mkdir {}_all1Mb_sbams'.format(pop)
        subprocess.run(mkdir_cmd, shell=True)

        logging.info("Making output directory")
        out_cmd = 'mkdir {}_all1Mb_scan_out'.format(pop)
        subprocess.run(out_cmd, shell=True)

        #change logger info here
        logging.info("Converting mEQTL file to .dat files")
        run_cmd = 'python3 run_scripts/make_run_scripts_01.py --geno {} --pheno {} --genemap {} --pop {} --outdir {}_all1Mb_sbams'.format(geno_folder, phenofile, genemapfile, pop, pop)
        subprocess.run(run_cmd, shell=True)

        #work on timing between steps to prevent the program from going over steps before files are ready
        #do we need a logger here?
        nohup_cmd = 'bash nohup_01.txt'
        subprocess.run(nohup_cmd, shell=True)

        logging.info('Running Batch Scan')
        batch_cmd = 'python3 02_all1MbSNPs_batch_scan.py --pop {}'.format(pop)
        subprocess.run(batch_cmd, shell=True)

        logging.info("Run nohup batch scan ")
        batch2_cmd = 'run_scripts/run_02_all1MbSNPs_batch_scan.sh {} &'.format(pop)
        subprocess.run('batch2_cmd, shell=True')

        #add logger info
        logging.info("")
        concat_cmd = 'python3 02b_concat_scan_out_bf_files.py --pop {}'.format(pop)
        subprocess.run(concat_cmd, shell=True)


        logging.info("Running Torus shell script")
        torus_cmd = 'bash 03_all1MbSNPs_torus.sh {} {} {}'.format(geno_folder,genemapfile,pop)
        subprocess.run('torus_cmd, shell=True')

        logging.info('Running DAP-G')
        dapg_cmd = 'bash run_scripts/run_04_all1MbSNPs_batch_dapg.sh {}'.format(pop)
        subprocess.run(dapg_cmd, shell=True)

        logging.info("Running make Vcf")
        vcf_cmd = 'bash run_/run_05_make_vcf.py {} {}'.format(geno_folder,pop)
        subprocess.run(vcf_cmd, shell=True)

        logging.info("Running fastenloc shell script")
        fnc_cmd = 'bash 06_all1MbSNPs_make_fastenloc_anot.sh {}'.format(pop)
        subprocess.run(fnc_cmd, shell=True) #Run script 06
    
    if gwasSS:
        ##can add logger here too
        ##flag here to tell which chromosome to look at? 
        r_cmd = 'Rscript 07a_sumstats_names.R {}'.format(gwasSS)
        subprocess.run(r_cmd)
        dblocks_cmd = 'python3 07_prep_sumstats_1000G_LDblocks.py --ldblocks {} --s {} --pop {} --annot {}_all1Mb_fastenloc.eqtl.annotation.vcf.gz --outprefix {}'.format(LD, gwasSS[i], pop, pop, gwas_prefix[i])
        subprocess.run(dblocks_cmd)
        torush_cmd = 'bash 08_gwas_zval_torus.sh {} {}'.format(gwas_prefix[i],pop)
        subprocess.run(torush_cmd)
        fastlc_cmd =  'bash 09_all1MbSNPs_fastenloc.sh {} {}'.format(gwas_prefix[i],pop)
        subprocess.run(fastlc_cmd)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logFormatter = '%(message)s'
    logging.basicConfig(filename='ProgressLogger.log', format=logFormatter, level=logging.DEBUG)
    main()
