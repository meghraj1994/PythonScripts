def mean(*args):
    return sum(args)/len(args)



print(mean(1,2,3,4,5,5,5))         # retunrn tuple when 



#function with named or key word args ie a=3, b=4 as params

def mean_name(**kwargs):
    return kwargs
    


print(mean_name(a=1, b=2, c=4))          #returns disctonary