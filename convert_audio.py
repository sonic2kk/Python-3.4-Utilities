#/usr/bin/env python

# Importing the OS module.
import os

# Importing the PyDub library to convert the audio files.
from pydub import AudioSegment


# Converter class.
class Convert():
	# Init method.
	def __init__(self):
		# Extension, extension to change and directory variable.
		self.extension = input("What extension should I convert to? ")
		self.extension_to_look_for = input("What extension should I look for? ")
		self.directory = input("What directory are the file(s) located? ")

		# Calling the main method. This does all the heavy lifting.
		self.main()

	def main(self):
		# Replacing "~" with the home directory of the user.
		if self.directory.startswith("~"):
			self.directory = self.directory.replace("~", os.path.expanduser("~"))

		# Changing into the directory the user specified.
		os.chdir(self.directory)

		# Looping through all files in our current directory.
		for f in os.listdir():
			# If our file does not begin with "."
			
			# This is because on some operating systems, files BEGINNING with
			# "." are hidden files, are are usually meant to be ignored as they
			# are mainly (or only) used by the system. On OS X, an example would
			# be the ".DS_STORE" file.
			if not f.startswith("."):
				# Printing the file we are converting.
				print("Converting: " + f + "...")

				# Loading the file using PyDub.
				file_to_convert = AudioSegment.from_file(f, self.extension_to_look_for)

				# Converting the file using PyDub.
				file_to_convert.export(f, format=self.extension)

				# Printing a success message. This will only be printed if the
				# conversion is successful.
				print("Converted " + f + " Successfully!")


# Creating a "Convert" object from the "Convert" class, and
# calling it "c".
c = Convert()