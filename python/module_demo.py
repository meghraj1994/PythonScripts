import time
import os


while True:
    if os.path.exists("vegetable.txt"):      # check if file is exist or not goto read me module to learn more
        with open("vegetable.txt") as my_vegi:
            content = my_vegi.read()
    else:
        print("file doesnot exist")

    time.sleep(10)

    print(content)