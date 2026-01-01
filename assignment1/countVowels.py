# Ask the user to input a word and count the number of vowels and consonants using a function.
def checkvc(string):
    v=0
    c=0
    vowels="aeiouAEIOU"
    for i in string:
        if i in vowels:
            v+=1
        else:
            c+=1
    print("Vowels:",v)
    print("Consonants:",c)

word=input("Enter a word")
checkvc(word)