#Inverted index, indexes line and word number of words in a document 

import os.path

#Search the doc dictionary for string
def SearchIndex(string, docs):
	for files in docs:
		if string in files[1]:
			occurances = files[1][string]
			print("%s occurs %d times in %s" % (string, len(occurances), files[0]))
			for occurance in occurances:
				print("	Line: %d and Word: %d" % (occurance[0], occurance[1]))
		else:
			print ("%s not in %s" % (string,files[0]))
	return

#Returns a dictionary with words and a list of their indexes
def Parse(string):
	windex = dict()
	linecount = 1
	with open(string) as f:
		for line in f:
			index = 1
			for word in line.split():
				for char in '?.!/;:@#$%^&*()-=_+{}][:"<>,':
					word = word.replace(char, "")
				if word in windex:
					windex[word].append((linecount, index))
				else:
					windex[word] = [(linecount, index)]
				index += 1
			linecount += 1
	return windex

#Checks for valid or existing file
def CheckFile(string, docs):
	if not os.path.exists(filename):
		return 0
	for files in docs:
		if string in files:
			return 0
	return 1

if __name__ == '__main__':
	documents = []
	while 1:
		string = input("Enter s to search, a to add file, and q to quit: ")
		if string == "s":
			if not documents:
				print ("No documents to search")
				continue
			word = input("Enter a word: ")
			SearchIndex(word, documents)
		elif string == "a":
			filename = input("Enter a filename: ")
			if CheckFile(filename, documents) == 1:
				windex = Parse(filename)
				documents.append((filename, windex))
				print ("Document successfully added")
			else:
				print ("Document error or already added")
		elif string == "q":
			print("Quiting")
			break
		else:
			print("WHAT ARE YOU DOING?")