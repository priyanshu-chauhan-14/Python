num = [23,34,21,67,54,89]
sec = 0
maxi = 0
for i in num:
    if(maxi<i):
        sec = maxi
        maxi = i

print(f"Second largest element is {sec}")
