#Create a program that takes a list of numbers and returns the maximum, minimum, and average values.

n = input("Enter how many numbers you'll provide : ")
a_list = list()
for num in range(n) :
    num = input("Input the number : ")
    a_list.append(num)

    
print("Your Numbers are: ", a_list)