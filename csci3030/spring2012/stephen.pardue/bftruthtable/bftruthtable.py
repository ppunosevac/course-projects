#!/usr/local/bin/python2.5
import argparse

from asciitruthtable import ascii_tables
from latextruthtable import latex_tables


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(
		description="generates truth tables for boolean functions",
		epilog="By Stephen Pardue. Fear the pandas")
	
	parser.add_argument(
		"function", metavar="fn", type=str, nargs="+",
		help="boolean function(s) to generate the table(s) for")
		
	parser.add_argument(
		"--ascii", dest="ascii", action="store_const", 
		const=True,
		help="output the table(s) to stdout in ascii format"
		)
		
	parser.add_argument(
		"--latex", dest="latex", action="store_const",
		const=True,
		help="output the table(s) to stdout in LaTex format")
	
	
	args = parser.parse_args()
	
	if args.ascii:
		ascii_tables(args.function)
	
	if args.latex:
		latex_tables(args)
		
	
	

	
	

	
	
	
	
