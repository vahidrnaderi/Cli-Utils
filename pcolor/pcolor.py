#!/usr/local/bin/python
'''Linux cat command simulator'''


def pcolor(mod: str, color: str) -> str:
    '''Return python ANSI color code for (f)oreground and (b)ackground
        from the color name 
    '''

    argColor = color.lower().capitalize()
    mod = mod.lower()

    if mod=='f':
        if argColor=='Black':	
            return '\033[1;30m'
        if argColor=='Red': 	
            return '\033[1;31m'
        if argColor=='Green':	
            return '\033[1;32m'
        if argColor=='Yellow':	
            return '\033[1;33m'
        if argColor=='Blue':	
            return '\033[1;34m'
        if argColor=='Magenta': 	
            return '\033[1;35m'
        if argColor=='Cyan':	
            return '\033[1;36m'
        if argColor=='White': 	
            return '\033[1;37m'
        if argColor=='Default': 	
            return '\033[1;39m'
        if argColor=='Reset':	
            return '\033[1;0m'
    elif mod=='b':
        if argColor=='Black':    
            return '\033[1;40m'
        if argColor=='Red':      
            return '\033[1;41m'
        if argColor=='Green':    
            return '\033[1;42m'
        if argColor=='Yellow':   
            return '\033[1;43m'
        if argColor=='Blue':     
            return '\033[1;44m'
        if argColor=='Magenta':  
            return '\033[1;45m'
        if argColor=='Cyan':     
            return '\033[1;46m'
        if argColor=='White':    
            return '\033[1;47m'
        if argColor=='Default':  
            return '\033[1;49m'
        if argColor=='Reset':    
            return '\033[1;0m'

if __name__ == "__main__":
    
    # Read arguments from the command line method 2
    import argparse

    parser = argparse.ArgumentParser(
                description='Give mod and color name as arguments'
           )
    parser.add_argument(
                'mod', 
                type=str, 
                help='f for foreground or b for background'
            )
    parser.add_argument(
                'colorName', 
                type=str, 
                help='Color name'
            )

    
    args = parser.parse_args()
    
    print(pcolor(args.mod, args.colorName) + " " + args.colorName)
