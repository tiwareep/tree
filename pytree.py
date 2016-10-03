#!/usr/bin/env python3
import sys
import os
import re

numDir = 0
numFile = 0

#Main function
def tree(startpath, indentation=""):
	files = []
	global numDir
	global numFile
	for i in os.listdir(startpath):
		if(i[0] != "."):
			files.append(i)
	files = sorted(files, key=sort)

	for i in range(len(files)):
		if i == len(files) - 1:
			print(indentation + "-- "+ files[i])
		else:
			print(indentation + "|-- "+ files[i])

		subdir = startpath + "/" + files[i]

		if os.path.isdir(subdir):
			numDir += 1
			if i == len(files) - 1:
				tree(subdir, indentation + "    ")
			else:
				tree(subdir, indentation + "|   ")
		else:
			numFile += 1

#Sort 
def sort(file): 
    punctuation = '_,;:?"\''
    return re.sub('[^A-Za-z0-9]+', '', file).lower()

#Printing the tree
if len(sys.argv) == 1:
	print (".")
	tree(".")
else:
	print (sys.argv[1])
	tree(sys.argv[1])
print("\n" + str(numDir) + " directorties, " + str(numFile) + " files")