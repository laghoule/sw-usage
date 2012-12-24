#!/usr/bin/python

# Written by Pascal Gauthier <pgauthier@nihilisme.ca>
# 12.22.2012 

import os
import sys

def main():
    "Swap usage by process"
    
    print "\nSwap usage"
    print "----------\n"

    total_swap = 0

    for procfile in os.listdir("/proc/"):
        if procfile.isdigit():
            smapfile = open("/proc/"+procfile+"/smaps", "r")
            total_swap_procfile = 0
            lines = smapfile.readlines()
            for line in lines:
                if line.find("Swap:") == 0:
                    swap_procfile = line.split()
                    if swap_procfile[1] > 0:
                        total_swap_procfile = int(swap_procfile[1]) + total_swap_procfile
            if total_swap_procfile > 0:
                print "PID %s: %s Kb" % (procfile, total_swap_procfile)
                total_swap = total_swap_procfile + total_swap
            smapfile.close()

    if total_swap > 0:
        print "\nTotal swap usage: %s Kb\n" % (total_swap)
        print "* not totally accurate for now\n"

    sys.exit(0)


if __name__ == "__main__":
    main()
