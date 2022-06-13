vowels=['a','e','i','o','u']
schar=[',','.','/','?',';',';','=','+','-','*','&','%','$','#','@','!']
cha=input("Enter a charecter:")
if cha in vowels:
    print("Vowel")
elif cha in schar:
    print("Special Charecter")
else:
    print("Consonant")