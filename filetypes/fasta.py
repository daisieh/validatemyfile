import re

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	if re.match(">", firstline):
		return True
	return False

def description():
	return "FASTA format for gene sequences"
