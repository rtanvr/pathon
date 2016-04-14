#Returns string in pig latin

vowels = 'AaEeIiOoUuYy'

class StringMan():
	def piglatin(self, string):
		pig = string.split()
		x = 0
		for char in pig:
			if char[0] in vowels:
				char += '-yay '
			else:
				char = char[1:len(char)] + char[0] + 'ay '

			pig[x] = char
			x += 1

		return "".join(pig)

if __name__ == '__main__':
	x = StringMan()
	string = input("Enter a string: ")
	print (x.piglatin(string))
	
