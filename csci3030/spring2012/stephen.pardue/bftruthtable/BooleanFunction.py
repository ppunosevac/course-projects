#!/user/bin/python
import re

DEBUG = False
#f(p,q,r) = ~p /\ ( q \/ ~r)
#g(p,q) = ~((p/\q) \/ ~(p \/ q))


class BooleanFunction:
	
	def __init__(self, funcStr):
		self.funcStr = funcStr
		self.error = False
	
		out = self.interpret_function()
		if out != None:
			self.error = out
			
		
	def interpret_function(self):
		"""
		Converts the user given function (self.funcStr) to python code storing it
		in self.func. 
		Saves the name of the func in self.name and the args in self.args.
		"""
		self.funcStr = self.funcStr.strip()
		rawFunc = self.funcStr.split("=")
		if len(rawFunc) == 1:
			return "Error 1: invalid function definition (missing a '=')"
		
		#find the name
		name = re.search("([a-zA-Z1-9].*?)\(", rawFunc[0])
		if name == None:
			return "Error 2: no function name"
		name = name.group(1)
		
		#find the functions
		args = re.search(name+"\((.*?)\)", rawFunc[0])
		if args == None:
			return "Error 3: couldn't find a function argument list"
		args = args.group(1).split(",")
		args = [arg.strip() for arg in args if arg != ""]
		
		#construct the function
		funcDef = rawFunc[1] 
		funcDef = funcDef.replace("/\\", " and ")
		funcDef = funcDef.replace("\\/", " or ")
		funcDef = funcDef.replace("~", " not ")
		
		preFunc = "lambda "
		for arg in args:
			preFunc+=arg+","
		preFunc+=":"
		
		func = preFunc+funcDef
		
		self.name = name
		self.args = args
		self.func = func
	
	def truth_table(self):
		"""returns a truth table of the function"""
		table = []
		code ="\n"+self.name+" = "+self.func+"\n"
		tabs = 1
		for arg in self.args:
			code+="for "+arg+" in [0,1]:\n"
			code+="\t"*tabs
			tabs+=1
		argsList = ",".join(self.args)
		funcCall = "int("+self.name+"("+argsList+"))"
		code+=("\t"*tabs)+"table.append([ " + argsList+ ","+ funcCall+"])"
		if DEBUG:
			print code
		exec(code)
		return table
		

	def latex(self):
		"""returns the function in latex format"""
		f = self.funcStr
		f = f.replace("/\\", " \\wedge ").replace("\\/", " \\vee ")
		f = f.replace("~", " \\sim ")
		return "\\begin{math}"+f+"\\end{math}"
		

		


if __name__ == "__main__":
	n = BooleanFunction("f(p,q,r) = ~p /\ ( q \/ ~r)")
	print n.truth_table()
	

	
	
	
	
	