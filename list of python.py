num = [1,2,3,454,55,.6,7,8,9,56,98,+9,898,45]

num.sort
print(num)
num.sort(reverse=True)
print(num)
print()
num.append(20)
print(num)

num.extend([25,65,98,45,36,52,14,58])
print(num)
print(num.index(45))