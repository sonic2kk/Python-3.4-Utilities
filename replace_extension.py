#!/usr/bin/env python

import os


class ReplaceExtension():
    def __init__(self):
        self.extension_to_change = input("What extension should I change? ")
        self.extension_to_look_for = input("What extension should I look for? ")
        self.directory = input("What directory are the file(s) located? ")

        if self.directory.startswith("~"):
        	self.directory = self.directory.replace("~", os.path.expanduser("~"))

        self.main()

    def main(self):
        os.chdir(self.directory)

        for f in os.listdir():
        	if f.endswith(self.extension_to_look_for):
        		fi = f.replace(self.extension_to_look_for, self.extension_to_change)
        		os.rename(f, fi)


c = ReplaceExtension()