#Count pi to Nth digit
import math

class Maths():
	def PI(self, numero):
		k = int(numero)
		pi = 0
		for i in range (0, k):
			pi += (1 / pow(16,i)) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
		#pi = 4 * math.atan(1)
		return round(pi, k)

if __name__ == '__main__':
	x = Maths()
	numero = input("Enter a number to couint PI to: ")
	print (x.PI(numero))