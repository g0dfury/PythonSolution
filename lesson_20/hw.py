import re
# # easy a
# date = '2013/09/09 09:09'
# date = 2012/09/18 12:10
# pattern = r'(\d{4})/\d{2}/\d{2}\s\d{2}:\d{2}'
# pattern = r'([0-9]{4})/[0-9]{2}/[0-9]{2}\s[0-9]{2}:[0-9]{2}'
# coincidence = re.search(pattern, date)
# if coincidence:
#     year = coincidence.group(1)
#     print(year)
# if 2012 >= int(year) > 1000:
#     print('Yes')
# else:
#     print('No')


# medium a
text = input()
res = re.sub(r'a([^a]+)a', r"!\1!", text)
print(res)




# hard a
# phone_number = input()
# pattern = (r'^\+?(747|707)[0-9]{7}$')
# coincidence = re.search(pattern, phone_number)
# if coincidence:
#     print('Hello')
# else:
#     print('Unknown')

