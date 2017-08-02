import re

# FASTA files are pairs of sequence IDs and sequences. 
# We're just validating that the first line starts with the sequence ID char ">"
# and that the second line does not. If things go haywire after that, it's not our problem.

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline()
	secondline = f.readline()

	if (re.match("^>", firstline) is not None) and (re.match("^>", secondline) is None):
		return True
	
	return False

def description():
	return "FASTA format for gene sequences"
