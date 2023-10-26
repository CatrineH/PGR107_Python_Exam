"""
                                                                                            Candidatenr: 1017
Note!

I have chosen not to comment the code explicitly,
but instead I have converted "comments" to variables, methods and class names to make the code self-explanatory.
I have also used a visual separator or divider to improve the readability and organization of the output.
Maybe this isn't the best way to practice. But in this case I find it easier to check/control the code 
and understand it this way.

"""

def occur_characters(string1, string2):
    return set(string1) & set(string2)

def unique_characters(string1, string2):
    return set(string1) ^ set(string2)

def non_occurring_characters(string1, string2):
    all_chars = set("abcdefghijklmnopqrstuvwxyz")
    s1_chars = set(string1)
    s2_chars = set(string2)
    return all_chars - (s1_chars | s2_chars)

def inoutput():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    print("--------------------------------------")
    print(f"Shared characters: {occur_characters(string1, string2)}")
    print("--------------------------------------")
    print(f"Unique characters: {unique_characters(string1, string2)}")
    print("--------------------------------------")
    print(f"Non-occuring characters: {non_occurring_characters(string1, string2)}")

inoutput()