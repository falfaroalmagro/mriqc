#!/usr/bin/env python

import re
import os
import glob
import time
import math
import logging
import sys,argparse,os.path
import scipy.stats as stats
from subprocess import check_output


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(): 


    parser = MyParser(description='Biobank asymmetrical metrics generator')
    parser.add_argument('-f', dest="fileName", type=str, nargs=1, help='File to check')
   
    argsa = parser.parse_args()

    fileName = argsa.fileName[0]

    if os.path.isfile(fileName):

        f=open(fileName)
        data=[float(x) for x in f.read().split()]
        res=[]
        if (len(data)!=15):
            print "NaN NaN NaN NaN NaN NaN NaN"
        else:
            for i in range(7):
                if (data[2*i] == 0) or (data[(2*i)+1] ==0):
                    res.append(float(100))
                else:
                    if data[2*i] > data[(2*i)+1]:
                        res.append(float(data[2*i]/data[(2*i)+1]))
                    else:
                        res.append(float(data[(2*i)+1]/data[2*i]))

            print " ".join(map(str,res))

    else:
        print "NaN NaN NaN NaN NaN NaN NaN"
   
             
if __name__ == "__main__":
    main()


