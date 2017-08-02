# Filetypes

To add new file types, create a new `<extension>.py` file in the filetypes directory. That python module should contain two methods:

* `check(filename)`
	This method should return True if the file is a valid file of this format, False otherwise.
	
* `description`
	This method should return a descriptive string about this file type.

# Examples

* fasta.py is the most basic of modules: it checks to see if the first two lines are formatted a certain way, using the re module.

* pdf.py is an example of a module using the python-magic/libmagic library; this is a quick way to add functionality that validates a MIME type before doing any optional extra checking.

* fa.py is an example of a redirecting module that merely calls the fasta module.
