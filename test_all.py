import validate
import os
import sys


def test_all():
	files = os.listdir('test')
	for file in files:
		print "checking " + file
		assert validate.validate(os.path.join('test',file)), "%s is INVALID FILE FORMAT" % file
