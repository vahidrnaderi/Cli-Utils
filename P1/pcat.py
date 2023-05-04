#!/usr/local/bin/python
''' Linux cat command simulator '''

def pcat(fileName):
    with open(fileName, "r") as f:
        text = f.read()
    print(text)


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

