# enter a string and the program will reverse the order and print it out

class StringMan():
	def reverse(self, string):

		tempword = ""

		for x in range(len(string)):
			tempword += string[len(string) - x - 1]

		return (tempword)

if __name__ == '__main__':
	x = StringMan()
	string = input("Enter a word: ")
	string = x.reverse(string)
	print (string)
