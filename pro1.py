import string


#reverse string
str = "python"
print(str[::-1])

a = string.ascii_letters

# shifting left the alphabet

b = a[1:] + a[0]

tab = string.maketrans(a, b)


# The message
msg = '''This text will be translated...'''

# The function translate() uses the translation table 
# created by maketrans() to translate the string
print(string.translate(msg, tab))
