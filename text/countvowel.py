#Counts vowel in a string

vowels = ['Aa','Ee','Ii','Oo','Uu','Yy']

class StringMan():
	def CountVowels(self, string):
		vowelscount = [0] * len(vowels)
		for i in range(len(string)):
			for y in range(len(vowels)):
				if string[i] in vowels[y]:
					vowelscount[y] += 1

		return vowelscount


if __name__ == '__main__':
	x = StringMan()
	string = input("Enter a string: ")
	count = [None] * len(vowels)
	count = x.CountVowels(string)
	print (', '.join(vowels))
	##print (', '.join(count))
	print(*count, sep=', ')
	totalcount = sum(count)
	print('Total Vowel Count:', totalcount)