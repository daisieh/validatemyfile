import validate
import os
import sys
import re

def test_all():
    files = os.listdir('test')
    for file in files:
        if re.match("^\.", file) is None:
            print("checking " + file)
            assert validate.validate(os.path.join('test',file)), "%s is INVALID FILE FORMAT" % file
    
    filetypes = os.listdir('filetypes')
    filename = os.path.join('test','test.vcf')
    for filetype in filetypes:
        extension = re.match("^([a-zA-Z0-9].+?)\.py$", filetype)
        if extension is not None and extension.group(1) != 'vcf':
            module = __import__("filetypes." + extension.group(1), globals(), locals(), ['check', 'description'])
            assert (module.check(filename) == False), "%s fails to reject invalid file" % filetype
if __name__ == '__main__':
    test_all()

