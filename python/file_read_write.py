#to read from some file >>help(open) => there are read r and write w mode
with open("fruits.txt") as myfile:
    conten = myfile.read()

print(conten)


#to write
with open("vegetable.txt", "w") as my_vegetable:            #note if you use this to add new line on exisiting file it will replace whole content
    my_vegetable.write("potato\ntomato\nbeans")


#to not replace exitin
with open("vegetable.txt", "a+") as my_vegetable:        #a+ for read and write without replcaing original content
    my_vegetable.write("\nokra  ")   
    my_vegetable.seek(0) #to see cursor to 0th position
    con = my_vegetable.read() 

print(con)