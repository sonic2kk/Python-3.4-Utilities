#!/usr/bin/env python

# Importing the OS module.
import os


# ReplaceExtension class.
class ReplaceExtension():
    # Init method.
    def __init__(self):
        # Extention to change, extension to look for and directory.
        # variables
        self.extension_to_change = input("What extension should I change? ")
        self.extension_to_look_for = input("What extension should I look for? ")
        self.directory = input("What directory are the file(s) located? ")

        # Replacing the "~" symbol with the users home directory.
        if self.directory.startswith("~"):
        	self.directory = self.directory.replace("~", os.path.expanduser("~"))

        # Calling the main method, which does all the heavy lifting
        self.main()

    def main(self):
        # Changing into the directory that the user has specified
        os.chdir(self.directory)

        # Looping through all directories in our current directory
        for f in os.listdir():
            # If the file ends with the extension we are looking for
        	if f.endswith(self.extension_to_look_for):
                # Storing a replaced version of our file in a string.
                # The reason for this is because in Python, Strings are
                # immutatible, meaning they cannot be changed. To work
                # around this, we store what the string would read in
                # a variable. This means that this does not replace the
                # the extension of the file in this line.
        		fi = f.replace(self.extension_to_look_for, self.extension_to_change)

                # Instead, this is done here. This uses the OS module to rename
                # the file, since strings are not mutatible from within Python,
                # we edit it on a system level (or on an OS (Operating System)
                # level).
        		os.rename(f, fi)


# Creating an instance of the "ReplaceExtension" class, calling it "re".
re = ReplaceExtension()