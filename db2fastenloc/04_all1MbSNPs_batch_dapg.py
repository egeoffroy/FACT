#!/usr/bin/python3
'''run dap-g using db SNPs for each gene'''
import os
import argparse
import sys
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Run dap-g using all SNPs for each gene')
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    return parser.parse_args(args)
args = check_arg(sys.argv[1:])
pop = args.pop
datlist = os.listdir(path=pop+'_all1Mb_sbams')

outfile = open(pop+"_all1Mb_batch_dap.cmd","w")
os.system("mkdir " +pop+"_all1Mb_dap_out")
for f in datlist:
    ens = f[:-4]
    outfile.write("/usr/local/bin/dap-g -d "+pop+"_all1Mb_sbams/" + f + " -t 4 -p "+pop+"_all1Mb_priors/" + ens + ".prior -o "+pop+"_all1Mb_dap_out/" + ens + ".fm.out\n")

#consider adding -ld_control flag, default is -ld_control 0.25
