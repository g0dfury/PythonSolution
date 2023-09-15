import re
# easy a
# text = input()
# print(re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}', text))


# easy b    ( х )
# text = input()
# pattern = re.findall(r'\b[aeiuoy][a-z]*\b', text, flags=re.IGNORECASE)
# print(pattern)

# medium a
# string = input()
# print(bool(re.search(r'\d$', string)))

# medium b

# text = input()
# res = re.search(r'\d', text)
# print(res.group(0))
# print(f'Index: {res.start()}')  
# .start()     
# .end()
# .span()


# hard a
# text = 'Human beings are nothing but a medium of the general process of carrying out life. They do want to live in peace, but want to win it over by war because ultimately victory is what brings them peace'
# print(re.findall(r'\b[a-zA-Z]{5}\b', text))


# hard b

# kebab case: my-first-name
# CamelCase: MyFirstName
# snake_case: my_first_name


CamelCase = input()
snake_case = re.sub(r'([A-Z])', r'_\1', CamelCase)[1:].lower()
print(snake_case)