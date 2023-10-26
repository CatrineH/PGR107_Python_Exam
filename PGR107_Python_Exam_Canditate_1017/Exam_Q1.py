"""
                                                                                            Candidatenr: 1017
Note!

I have chosen not to comment the code explicitly,
but instead I have converted "comments" to variables, methods and class names to make the code self-explanatory.
I have also used a visual separator or divider to improve the readability and organization of the output.
Maybe this isn't the best way to practice. But in this case I find it easier to check/control the code 
and understand it this way.

"""

def create_redact_words(original_file, sensitive_words_file, redacted_file):
    try:
        with open(original_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {original_file} does not exist.")
        return

    try:
        with open(sensitive_words_file, 'r') as f:
            sensitive_words = f.read().split()
    except FileNotFoundError:
        print(f"Error: {sensitive_words_file} does not exist.")
        return

    redacted_content = content
    for word in sensitive_words:
        redacted_content = redacted_content.replace(word, '*' * len(word))

    try:
        with open(redacted_file, 'w') as f:
            f.write(redacted_content)
        print("---------------------------------------------------------")
        print(f"Perfect! The redacted file '{redacted_file}' has been created.")
    except:
        print("Error occurred while creating the redacted file.")

original_file = input("Enter the filename to save the original text file (txt): ")
sensitive_words_file = input("Enter the filename to save the sensitive words file (txt): ")
redacted_file = input("Enter the filename to save the redacted file (txt): ")
print("---------------------------------------------------------")

original_content = input("Enter the original text: ")
try:
    with open(original_file, 'w') as f:
        f.write(original_content)
    print("---------------------------------------------------------")    
    print(f"Perfect! The original file '{original_file}' has been created.")
except:
    print("Error occurred while creating the original file.")
print("---------------------------------------------------------")

sensitive_words_content = input("Enter the sensitive words (separated by spaces): ")
sensitive_words = sensitive_words_content.split()
try:
    with open(sensitive_words_file, 'w') as f:
        f.write("\n".join(sensitive_words))
    print("---------------------------------------------------------")
    print(f"Perfect! The sensitive words file '{sensitive_words_file}' has been created.")
except:
    print("Error occurred while creating the sensitive words file.")

# Extra - Ask user y/n open file
create_redact_words(original_file, sensitive_words_file, redacted_file)
print("---------------------------------------------------------")
open_redacted_file = input("Do you want to open the redacted file? (y/n): ")
if open_redacted_file.lower() == "y":
    try:
        with open(redacted_file, 'r') as f:
            redacted_content = f.read()
        print("---------------------------------------------------------")
        print(f"Redacted Content:")
        print(redacted_content)
    except FileNotFoundError:
        print(f"Error: {redacted_file} does not exist.")
else:
        print("---------------------------------------------------------")
        print("Thank you for using the program. Have a great day!")