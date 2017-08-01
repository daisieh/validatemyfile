import re

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	if re.match("^(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.*)$", firstline):
		return True
	return False

def description():
	return "PED format is part of PLINK package"
