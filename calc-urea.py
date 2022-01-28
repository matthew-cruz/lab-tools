

import argparse #for parsing arguments
import sys #take in inputs
import numpy as np


# read command line input to define arguments
def process_command_line(argv):
    """ read command line input to define arguments.
    """
    parser = argparse.ArgumentParser() #defines an object as 'parser'
    input_args = parser.add_argument_group("Input Settings") #add the arguments to parser
    input_args.add_argument('--blank', required=True, 
                            help="The refractive index of the buffer without urea.")
    input_args.add_argument('--urea', required=True, 
                            help="The refractive index of the buffer with urea.")
    args = parser.parse_args(argv[1:]) #parse through the object to define what the arguments are
    return args

#calculate the concentration of urea in buffer
def urea_conc(blank_nu, urea_nu):
    """ calculate the concentration of urea in buffer
    """
    blank_nu = np.float(np.asarray(blank_nu))
    urea_nu = np.float(np.asarray(urea_nu))
    delta = urea_nu - blank_nu
    square = delta ** 2
    cube = delta ** 3
    conc_urea = 117.66 * delta + 29.753 * square + 185.56 * cube
    return conc_urea

#this is the main command that I want run i.e. executable
def main(argv):
    args = process_command_line(argv)
    print("%.4f" % urea_conc(args.blank, args.urea))
    return None
#this line will execute the script as specified in 'main'
if __name__ == "__main__":
    sys.exit(main(sys.argv))