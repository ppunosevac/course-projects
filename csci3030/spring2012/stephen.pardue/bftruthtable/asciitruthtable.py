from BooleanFunction import BooleanFunction

def ascii_truth_table(bf):
	out = ""
	table = bf.truth_table()
	
	out+=" "
	out+=" | ".join(bf.args)+" | "+bf.name+"\n"
	out+="_"*len(out)+"\n"
	for row in table:
		out+=" "
		out+=" | ".join([str(n) for n in row])+"\n"
	return out
	
def ascii_tables(fns):
	for fn in fns:
		f = BooleanFunction(fn)
		print(fn)
		if not f.error:
			print(ascii_truth_table(f))
		else:
			print("Error: "+f.error)