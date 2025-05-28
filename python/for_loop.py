
nums = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.7,9.9]

# for num in nums:
#     if num > 5:
#         print(round(num))
#     else:
#         print(0)


# for letter in 'hello':
#     print(letter)


#iterate over disctionary

my_distionary =  {"A":1, "B":2, "C":3, "D":4}

# for item  in my_distionary.items():
#     print(item)


for key, value in my_distionary.items():
    # print(f"Key : {key}, Value: {value}")
    if key == "C":
        print(value)



for value in my_distionary.values():
    print(value)

