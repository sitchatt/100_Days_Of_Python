#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇 

sum_height = 0
for i in student_heights :
  sum_height += i
print (f"Your Sum Height is", (sum_height))

sum_number = 0
for j in student_heights :
  sum_number += 1
print (f"Your Sum Number is", sum_number)

avg = round(sum_height / sum_number)
print (avg)


#Write your code below this row 👇
