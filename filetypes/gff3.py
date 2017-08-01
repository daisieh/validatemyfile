import re

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	if re.match("##gff-version", firstline) is None:
		return False
	line = f.readline()
	pieces = re.split('\t', line)
	if len(pieces) == 9:
		return True
	return False

def description():
	return "GFF3 file for genome annotation"
