import re

def check(filepath):
	f = open(filepath, 'r')
	line = f.readline()
	
	# eat the header
	while re.match("^#", line):
		line = f.readline()
	
	pieces = re.split('\t', line)
	if len(pieces) > 8:
		return True
	return False

def description():
	return "VCF: variant call format for genotype specification"
