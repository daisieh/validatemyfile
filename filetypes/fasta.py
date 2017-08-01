import re

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	secondline = f.readline()
	if (re.match(">", firstline) is not None) and (re.match(">", secondline) is None):
		return True
	return False

def description():
	return "FASTA format for gene sequences"
