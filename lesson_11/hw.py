# easy a            #во время итерации нельзя менять размер сета и листа
# num = set(map(int, input().split()))
# for i in num:
#     if i % 3 != 0:
#         print(i, end=" ")


# easy b 
# st = set(map(int, input().split()))
# ans = set ()
# for el in st:
#     num = el
#     while el >= 1:
#         el /= 2
#         if el == 1:
#             ans.add(num)
# print(ans)


# medium a
# num = set(map(int, input().split()))
# max_el = max(num)
# min_el = min(num)
# print("max element is ", max_el)
# print("min element is ", min_el)


# # medium b 
# num = list(map(int, input().split()))
# st = set(num)
# print ("Unique elements: ", len(st)) 

# # hard a
# num = list(map(int, input().split()))  ### создал set
# unique = set(num)
# for numbers in unique:
#     if numbers in unique:
#         print("NO")
#     else:
#         print("YES")


# hard a V20 
numbers = list(map(int, input().split()))
st = set()
for el in numbers:
    if el in st:
        print("YES")
    else:
        print("NO")
        st.add(el)

# hard b
n = int(input())
st = set()

for i in range (n):
    text = input()
    words = text.split()
    st.update(words)
print(len(st))