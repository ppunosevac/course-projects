##Copyright (c) 2012, Stephan Pardue
##Contributions include 
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without
##modification, are permitted provided that the following conditions are met: 
##
##1. Redistributions of source code must retain the above copyright notice, this
##   list of conditions and the following disclaimer. 
##2. Redistributions in binary form must reproduce the above copyright notice,
##   this list of conditions and the following disclaimer in the documentation
##   and/or other materials provided with the distribution. 
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
##ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
##WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
##DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
##ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
##(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
##ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
##(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
##SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##
##The views and conclusions contained in the software and documentation are those
##of the authors and should not be interpreted as representing official policies, 
##either expressed or implied, of the FreeBSD Project.

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
	

	
	
	
	
	
