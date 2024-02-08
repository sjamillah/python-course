#!/usr/bin/python3
#Script to calculate the average height using for loop

print("Calculate the average student height")
student_heights = input("Input a list of students' heights as integers:")
new_student_heights = student_heights.split() #changes the heights from strings to a list
length_heights = len(new_student_heights) #total number of inputted lengths
total_sum = 0
for x in range(0, length_heights):
  new_student_heights[x] = int(new_student_heights[x]) #changes height to int datatype

  total_sum += new_student_heights[x] #adds the heights based on the range of x

average_height = round(total_sum / length_heights)
print(f"The list of the heights is:  {new_student_heights}")
print(f"The total of heights is: {length_heights}")
print(f"The sum is: {total_sum}")
print(f"The average height is: {average_height}")

