#string transform funtions
#captalize
a= "i am jyothi"
print(a.capitalize())
#title
a = "i am jyothi"
print(a.title())
#uppercase
a = " jyothi korrapati"
print(a.upper())
#lowercase
a= "JYOTHIKORRAPATI"
print(a.lower())
#casefold
a = "PYTHON IS A DYNNAMICLLY TYPED"
print(a.casefold())

#swapcase
a= "JyothiKorrapati"
print(a.swapcase())

#string check functions
#is numeric
a = "Jyothi"
print(a.isnumeric())
a = "123"
print(a.isnumeric())
#is alnumer
a = "hello1234"
print(a.isalnum())
a = "jyothi45677"
print(a.isalpha())
a = "#"
print(a.isalpha())
#isdecimal
a = "hello"
print(a.isdecimal())
a = "12"
print(a.isdecimal())
a = "12.4"
print(a.isdecimal())
#is digit
a = "jyo12334"
print(a.isdigit())
a = "167899"
print(a.isdigit())
a = "12.78"
print(a.isdigit())
#isaassci
a = "Jyothi"
print(a.isascii())
a = "$$$$$$$$$"
print(a.isascii())
# is upper
a = "hello"
print(a.isupper())
a = "HELLO"
print(a.isupper())
#is lower
a = "JYOTHI"
print(a.islower())
a = "jyothiKorrapati"
print(a.islower())
a = "hello"
print(a.islower())

#is space
a = "jyo  123"
print(a.isspace())
a = "      "
print(a.isspace())

#is idendifies
a = "jyothi"
print(a.isidentifier())
a = "jyo8900"
print(a.isidentifier())
a = "12234555"
print(a.isidentifier())
a= "##"
print(a.isidentifier())
# isprintable
a = "jyothi"
print(a.isprintable())
a = "123"
print(a.isprintable())
#is title
a = "Hello"
print(a.istitle())
a = "hello jyoti"
print(a.istitle())