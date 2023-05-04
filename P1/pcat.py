#!/usr/local/bin/python
''' Linux cat command simulator '''

def ANSIColor(mod, color):
    
    if mod=='f':
        if color=='Black':	
            return '\033[1;30m'
        if color=='Red': 	
            return '\033[1;31m'
        if color=='Green':	
            return '\033[1;32m'
        if color=='Yellow':	
            return '\033[1;33m'
        if color=='Blue':	
            return '\033[1;34m'
        if color=='Magenta': 	
            return '\033[1;35m'
        if color=='Cyan':	
            return '\033[1;36m'
        if color=='White': 	
            return '\033[1;37m'
        if color=='Default': 	
            return '\033[1;39m'
        if color=='Reset':	
                return '\033[1;0m'
    elif mod=='b':
        if color=='Black':    
            return '\033[1;40m'
        if color=='Red':      
            return '\033[1;41m'
        if color=='Green':    
            return '\033[1;42m'
        if color=='Yellow':   
            return '\033[1;43m'
        if color=='Blue':     
            return '\033[1;44m'
        if color=='Magenta':  
            return '\033[1;45m'
        if color=='Cyan':     
            return '\033[1;46m'
        if color=='White':    
            return '\033[1;47m'
        if color=='Default':  
            return '\033[1;49m'
        if color=='Reset':    
                return '\033[1;0m'

def pcat(fileName):
    import os, curses, sys
    

    with open(fileName, "r", encoding="utf-8") as f:
        title1 = f"\n {ANSIColor('f', 'White')} File status:\n"
        line1 = f"{ANSIColor('f', 'Green')}     File Name ={ANSIColor('f', 'White')} {fileName} \n"
        line2 = f"{ANSIColor('f', 'Green')}     File Size ={ANSIColor('f', 'White')} {os.stat(fileName).st_size} Byte \n "
        divider1 = f"   ###################### \n\n"
        
        print(f"{title1}{line1}{line2}{divider1}")              
             
              
        i = 0
        for line in f:
            i+=1
            print(f"{ANSIColor('f', 'Blue')}{i:3}{ANSIColor('f', 'White')} {line}", end='')


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

