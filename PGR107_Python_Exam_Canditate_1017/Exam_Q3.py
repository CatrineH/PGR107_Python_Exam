"""
                                                                                            Candidatenr: 1017
Note!

I have chosen not to comment the code explicitly,
but instead I have converted "comments" to variables, methods and class names to make the code self-explanatory.
I have also used a visual separator or divider to improve the readability and organization of the output.
Maybe this isn't the best way to practice. But in this case I find it easier to check/control the code 
and understand it this way.

"""

def is_palindrome(string):
    
    string = string.lower()
    
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

def check_word():
        user_input = input("HELLO, WELCOME!\n\nENTER A WORD: ")
        print("--------------------------------------")
        if is_palindrome(user_input):
            print(f"{user_input} /// WOW, it is a palindrome!")
        else:
            print(user_input)   
            print("Sorry, this is not a palindrome.\n\nHint! A palindrome is identical forward and backwards.")
while True:            
        check_word()
        print("--------------------------------------")
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() != "y":
            break   
print("--------------------------------------")
print("Goodbye from the world of palindrome!")    
print("--------------------------------------")