def mean(input):
    if isinstance(input, dict) :
        the_mean = sum(input.values()) / len(input)
    else:
        the_mean=sum(input)/len(input)

    return the_mean



student_dic = {"A":1, "B":2, "C":3, "D":4}
print(mean(student_dic))
print(mean([1,2,3,4,5]))