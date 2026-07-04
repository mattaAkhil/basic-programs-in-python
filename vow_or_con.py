vow=['a','e','i','o','u']
n=input("enter a character:")
n1=n.lower()
if n1 in vow:
    print(f"{n} is a vowel")
else:
    print(f"{n} is a consonant")    