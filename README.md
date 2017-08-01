# validatemyfile
Validates files against a library of known file types/formats

To run, just execute `python validate.py <filename>`

To add new file types, create a new `<extension>.py` file in the filetypes directory. That python module should contain two methods:

* `check(filename)`
	This method should return True if the file is a valid file of this format, False otherwise.
	
* `description`
	This method should return a descriptive string about this file type.
	
Also add a small test file of the new file type in the `test` directory.

When you've created your new file module, please send me a pull request to incorporate it into the main library.
