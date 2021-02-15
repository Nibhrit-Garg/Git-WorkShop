# function to check if given number is prime 
def prime_no(n):
	if n == 1 or n == 2:
		return True
	c = 0
	for i in range( 2 , n**0.5 + 1):
		if n % i == 0:
			c = 1
			return False
			break
	if c == 0:
		return True
N = int(input())
if prime_no(N):
	print('prime')
else:
	print ('no prime') 


