#!/usr/bin/env python

import re
import os
import sys

def main():
    filename = sys.argv[1]
    file_name, extension = os.path.splitext(sys.argv[1])
    
    # look for extension's module
    module = __import__("filetypes" + extension, globals(), locals(), ['check', 'description'])
    print module.description()
    print module.check(filename)
    
    

if __name__ == '__main__':
    main()

