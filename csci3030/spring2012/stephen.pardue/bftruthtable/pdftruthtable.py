from BooleanFunction import BooleanFunction
from latexTemplate import latexTemplate

def latex_tables(args):
	bfs = [BooleanFunction(fn) for fn in args.function]
	texTemp = latexTemplate()
	texTemp.bfs = bfs
	return texTemp.respond()


	
	
	
	
	
