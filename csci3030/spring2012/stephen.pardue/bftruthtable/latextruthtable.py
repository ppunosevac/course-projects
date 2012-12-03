from BooleanFunction import BooleanFunction
from latexTemplate import latexTemplate

def latex_tables(args):
	bfs = [BooleanFunction(fn) for fn in args.function]
	texTemplate = latexTemplate()
	texTemplate.bfs = bfs
	print texTemplate


	
	
	
	
	
