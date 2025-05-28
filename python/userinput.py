def daily_temperature(input):
    if input == 5:
        print("Temperature is Moderate")
    elif input > 5:
        print("its hot outside")
    else:
        print("its cold outside")


user_input = float(input("Enter temperature : ")) # when we input python will take i/p as string so we need to convert it as num
daily_temperature(user_input)

#string formate
user_input = input("Enter name : ")
messageOld = "Hello %s!" %user_input        #old way before python 3
message = f"hello {user_input}"
print(message)
print(messageOld)

#with two params
name = input("Enter name :")
surname = input("Enter surname")

messageOld = "Hello %s %s" %(name, surname)
print(messageOld)

message = f"Hello {name} {surname}"
print(message)
