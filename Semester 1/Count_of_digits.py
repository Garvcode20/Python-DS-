#print the count of digits in number:-

n = int(input("Enter any number: "))

count = 0

while(n > 0):
    count = count + 1
    n = n//10

print("Count of digits in", n, "is:", count)