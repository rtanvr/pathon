#See if string is a palindrome

class StringMan():
	def palindrome(self, string):
		for char in string:
			if string == string[::-1]:
				return "Palindrome"
			else:
				return "Not Palindrome"

if __name__ == '__main__':
	x = StringMan()
	string = input("Enter a string: ")
	print (x.palindrome(string))
