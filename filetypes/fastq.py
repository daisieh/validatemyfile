import re

# FASTQ files are formatted as pairs of sequence + quality scores, split as two parallel couplets:
# @SEQID
# sequence-of-length-x (poss split over lines)
# +
# quality-string-of-length-x (poss split over lines)

def check(filepath):
	f = open(filepath, 'r')
	firstline = f.readline().rstrip()
	if re.match("^[@>]", firstline) is None:
		return False
	
	secondline = f.readline().rstrip()
	line = f.readline().rstrip()
	while re.match("^\+", line) is None:
		secondline = secondline + line
		line = f.readline().rstrip()
		if line == '':
			return False

		
	if line == '':
		return False
	
	thirdline = line
	if thirdline != '+':
		return False
		
	fourthline = f.readline().rstrip()
	line = f.readline().rstrip()
	while re.match("^[@>]", line) is None:
		fourthline = fourthline + line
		line = f.readline().rstrip()
		if line == '':
			break
		
	if len(fourthline) != len(secondline):
		return False
	
	return True

def description():
	return "FASTQ format for gene sequences"
