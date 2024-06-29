#Create a program that takes a list of numbers and returns the maximum, minimum, and average values.

n = int(input("Enter how many numbers you'll provide : "))
a_list = list()
for num in range(n) :
    num = int(input("Input the number : "))
    a_list.append(num)

print("Your Numbers are: ", a_list)
print("Your Maximim number is: ", max(a_list))
print("Your Minimum number is: ", min(a_list))
print("Your Sum is: ", sum(a_list))
print("Your average is: ", sum(a_list)/len(a_list))
