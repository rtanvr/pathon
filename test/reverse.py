# enter a string and the program will reverse the order and print it out

word = input("Enter a word: ")

tempword = ""

for x in range(len(word)):
	tempword += word[len(word) - x - 1]

print (tempword)
