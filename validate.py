#!/usr/bin/env python

import re
import os
import sys

def main():
    filename = sys.argv[1]
    result = validate(filename)
    print(result[0])
    
def validate(filename):
    file_name, extension = os.path.splitext(filename)
    # look for extension's module
    module = __import__("filetypes" + extension, globals(), locals(), ['check', 'description'])
    print(module.description())
    return (module.check(filename),module.description())
    

if __name__ == '__main__':
    main()

