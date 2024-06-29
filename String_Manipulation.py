

def reverse_string_check_palindrome () :
    input_string = input ("Enter the string :")
    output_string = input_string[::-1]
    print(output_string)
    reverse_string_check_palindrome ()
    
    
reverse_string_check_palindrome ()