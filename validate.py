#!/usr/bin/env python

import re
import os
import sys

def main():
    filename = sys.argv[1]
    print validate(filename)
    
def validate(filename):
    file_name, extension = os.path.splitext(filename)
    # look for extension's module
    module = __import__("filetypes" + extension, globals(), locals(), ['check', 'description'])
    print module.description()
    return module.check(filename)  
    

if __name__ == '__main__':
    main()

