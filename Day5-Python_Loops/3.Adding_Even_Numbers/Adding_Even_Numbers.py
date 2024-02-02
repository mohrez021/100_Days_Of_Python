target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
# way 1
even_sum = 0
for num in range(2, target + 1, 2):
    even_sum += num
print(even_sum)

# way2
# even_sum = 0
# for num in range(0, target+1):
#     if num % 2 ==0:
#         even_sum += num
# print(even_sum)
