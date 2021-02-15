import os
import sys
import json


# I didn't want to use any libraries besides the ones built in
class ArgumentParser(object):
	def __init__(self, *arguments):
		self.arguments = arguments

	def parse(self, usage):
		if len(sys.argv) - 1 != len(self.arguments):
			print("Usage: " + usage)
			print("The arguments were wrongly specified")
			exit()

		else:
			items = {}
			for ind,itm in enumerate(self.arguments):
				items[itm] = sys.argv[ind + 1]

			return items

def get_all(myjson, key, filename):
	
	if type(myjson) == str:
		
		myjson = json.loads(myjson)
		
	if type(myjson) is dict:
		for jsonkey in myjson:
			if jsonkey == key:
				print("found the key: %s in %s" % (jsonkey, filename))
				#print(myjson[jsonkey])
			if ((type(myjson[jsonkey]) == list ) or (type(myjson[jsonkey]) == dict )) :
				get_all(myjson[jsonkey], key, filename)
			
	elif type(myjson) is list:
		for item in myjson:
			if type(item) in (list, dict):
				get_all(item, key,filename)

# Create a parser reference
parser = ArgumentParser("keyword", "directory")
args = parser.parse("python solution.py <keyword> <directory>")


rootdir = args["directory"]
import glob
items = list(set(glob.glob(rootdir + '**/**', recursive=True)))
for filename in items:
	if ".json" in filename:
		try:
			with open(filename, 'r') as data:
				string1 = data.read()
				get_all(string1, args["keyword"], filename)
			data.close()
		except Exception as e:
			print (e)
			print("Not able to open the file")
		
	