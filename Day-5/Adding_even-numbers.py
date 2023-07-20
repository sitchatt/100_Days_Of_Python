# Write a program to add all even number from 1-100 inclusively

#Write your code below this row 👇

#Method_1

even_number = 0

for i in range (0, 101, 2) :

 even_number += i

all_even = [(int(even_number))]
print (all_even)
print (type(all_even))

#even_list = [int(digit) for digit in str(all_even)]


highest_number = 0

for j in (all_even) :
  if j > highest_number :
    highest_number = j
print (f"The Sum of even numbers are as per method 1 : {highest_number}")

#Method 2

total = 0

for i in range (0, 101, 2) :

 total += i

print (f"The Sum of even numbers are as per method 3 : {total}")

#Method 3

total2 = 0

for k in range (1, 101) :
  if k % 2 == 0 :
    total2 += k
print (f"The Sum of even numbers are as per method 3 : {total2}")



 
