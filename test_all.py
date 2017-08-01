import validate
import os
import sys
import re

def test_all():
	files = os.listdir('test')
	for file in files:
		if re.match("^\.", file) is None:
			print "checking " + file
			assert validate.validate(os.path.join('test',file)), "%s is INVALID FILE FORMAT" % file
