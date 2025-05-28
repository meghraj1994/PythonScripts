import time
import os
import pandas


while True:
    if os.path.exists("vegetable.txt"):      # check if file is exist or not goto read me module to learn more
        data = pandas.read_csv("vegetable.txt")
        print(data.mean()) 
        print(data.mean()["str1"])  # to get mean of only one column
    else:
        print("file doesnot exist")

    time.sleep(10)
