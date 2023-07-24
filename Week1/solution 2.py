#Write a python script to enter any number and print the sum of its digit.
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
