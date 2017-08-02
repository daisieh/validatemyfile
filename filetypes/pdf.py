import re
import magic

def check(filepath):
    result = magic.from_file(filepath, mime=True)
    if re.match('application/pdf', result):
        return True
    return False

def description():
	return "PDF: portable document format"
