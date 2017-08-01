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

## Notes:
My philosophy is to make a file validator that basically acts as a sanity checker. Many genomics files are massive in size but are basically a long list of similarly-formatted lines. I'd like this validator to read just a few lines and decide if the file makes sense. Therefore, I am not interested in validating the *entire* file at this point (but maybe later!); I just want to have a quick tool that someone can run to see if a file could possibly be the type of file one thinks it is, based on its name.
