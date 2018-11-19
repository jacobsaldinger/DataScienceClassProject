#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rxncount.py
Counts fwd/rev rxns from CHEMKIN file

Handles the primary functions
"""

import sys
import argparse


def warning(*objs):
    """Writes a message to stderr."""
    print("WARNING: ", *objs, file=sys.stderr)

def parse_cmdline(argv):
    """
    Returns the parsed argument list and return code.
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = argparse.ArgumentParser()
    # parser.add_argument("-i", "--input_rates", help="The location of the input rates file",
    #                     default=DEF_IRATE_FILE, type=read_input_rates)
    parser.add_argument('-txtfile','--fname',help="Input the file path of the .txt file",default='./sampletext.txt')
    parser.add_argument('-f',"--forward" ,help="Whether to calculate only fwd reactions",action='store_true')

    args = None
    try:
        args = parser.parse_args(argv)
    except IOError as e:
        warning("Problems reading file:", e)
        parser.print_help()
        return args, 2

    return args, 0


def main(argv=None):
    """

    Parameters
    ----------
    Text file of all reactions

    Returns
    -------
    Number of forward reactions, number of reverse reactions, number of total reactions
    """
    args, ret = parse_cmdline(argv)
    if ret != 0:
        return ret
    #Open the text file and combine all text into string set equal to my data
    with open(str(args.fname), 'r') as myfile:
        data = myfile.read()
    #Count the number of forward and reverse reactions, this is done by counting characters
    #<,=,>
    #A forward reaction is denoted by '=>'
    #A reverse reaction is denoted by '='
    #A two way reaction is denoted by '<=>'
    #Thus forward rxn= # of '=>' + # of '<=>'
    #Reverse Reaction=# of '=' + # of '<=' - # of forward rxns
    #Total reactions=#F orward+# Reverse
    if args.forward==True:
        fwdrxn = data.count('=>')
        print('The number of fwd reactions is: {}\n'.format(fwdrxn))
        out = fwdrxn, None, None
    else:
        fwdrxn=data.count('=>')
        revrxn = data.count('=')+data.count('<=')-fwdrxn
        totrxn=fwdrxn+revrxn
        out=fwdrxn,revrxn,totrxn
        #Print results
        print('The number of fwd reactions is: {}\n'.format(fwdrxn))
        print('The number of rev reactions is: {}\n'.format(revrxn))
        print('The number of total reactions is: {}\n'.format(totrxn))
    return out  # success

if __name__ == "__main__":
    status = main()
    sys.exit(status)
