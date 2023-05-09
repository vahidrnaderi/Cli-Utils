#!/usr/local/bin/python
'''Linux cat command simulator with using pcoor module (using ANSI color)'''

import sys
sys.path.append('../')
from pcolor import pcolor

def pcat(fileName):
    '''Python cat command simulation'''


    import os, curses, sys, rich
    from rich.console import Console
    from rich.table import Table


    with open(fileName, "r", encoding="utf-8") as f:
        title1 = f"\n {pcolor.pcolor('f', 'White')} File status:\n"
        line1 = f"{pcolor.pcolor('f', 'Green')}     File Name ={pcolor.pcolor('f', 'White')} {fileName} \n"
        line2 = f"{pcolor.pcolor('f', 'Green')}     File Size ={pcolor.pcolor('f', 'White')} {os.stat(fileName).st_size} Byte \n "
        divider1 = f"   ###################### \n\n"
        
        print(f"{title1}{line1}{line2}{divider1}")              
        
        
        # read and print the contents of the file line by line
        i = 0
        for line in f:
            i+=1
            print(f"{pcolor.pcolor('f', 'Blue')}{i:3}{pcolor.pcolor('f', 'White')} {line}", end='')


if __name__ == "__main__":
    # Read arguments from the command line method 1
#    import sys
#    pcat(sys.argv[1])

    
    # Read arguments from the command line method 2
    import argparse

    parser = argparse.ArgumentParser(
                description='Read file and print it.'
           )
    parser.add_argument(
                'filename', 
                type=str, 
                help='the input file name'
            )

    
    args = parser.parse_args()

    pcat(args.filename)

