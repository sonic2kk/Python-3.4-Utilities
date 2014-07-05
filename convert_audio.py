#/usr/bin/env python

import os

from pydub import AudioSegment


class Convert():
	def __init__(self):
		self.extension = input("What extension should I convert to? ")
		self.extension_to_look_for = input("What extension should I look for? ")
		self.directory = input("What directory are the file(s) located? ")

		self.main()

	def main(self):
		if self.directory.startswith("~"):
			self.directory = self.directory.replace("~", os.path.expanduser("~"))

		os.chdir(self.directory)

		for f in os.listdir():
			if not f.startswith("."):
				print("Converting: " + f + "...")

				file_to_convert = AudioSegment.from_file(f, self.extension_to_look_for)

				file_to_convert.export(f, format=self.extension)

				print("Converted " + f + " Successfully!")


c = Convert()