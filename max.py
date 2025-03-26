x=0
max=0
array = []
while x<5:
    num = int(input("Enter the number: "))
    array.append(num)
    print(array[x])
    x+=1
    if max<num:
        max = num
    

print(max)