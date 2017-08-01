import re

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	pieces = re.split('\t', firstline)
	if len(pieces) == 9:
		return True
	return False

def description():
	return "GFF file for genome annotation"
