#!/usr/bin/python3
'''make file with batch commands to run dap-g scan for 1Mb SNPs within each gene'''
import os
import argparse
import sys
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Run dap-g scan for 1Mb SNPs within each gene')
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    return parser.parse_args(args)
args = check_arg(sys.argv[1:])
pop = args.pop
datlist = os.listdir(path=pop+'_all1Mb_sbams')

outfile = open(pop+"_all1Mb_batch_scan.cmd","w")
for f in datlist:
    ens = f[:-4]
    outfile.write("/usr/local/bin/dap-g -d "+pop+"_all1Mb_sbams/" + f + " --scan > "+pop+"_all1Mb_scan_out/" + ens + ".bf\n")
outfile.close()
