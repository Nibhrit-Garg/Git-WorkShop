# function to check if given number is prime or not
def is_prime(n):
    cur = 2
    while cur ** 2 <= n:
        if n % cur == 0:
            return false # error
        cur++
    return true # error

#this the edit i will do
if __name__ == "__main__":
    n = int(input())
    if is_prime(n):
        print("The number if prime!!")
    else:
        # correct the error here
        print(It is not prime)
