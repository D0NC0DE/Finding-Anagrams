# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

 
def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        print("The Strings are Anagrams")
    else:
        print("This strings are not Anagrams")

word = input ("Input a Word: ")
anagram = input("Input another Word, let me check if it is an Anagram: ")

find_anagram(word, anagram)
