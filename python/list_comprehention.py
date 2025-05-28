temperaturs = [221,222,234,345,344,343,343]

new_tems = [temp/10 for temp in temperaturs];

print(new_tems)

## using if in list comprehention , -999 means no valid value found
temps = [221,222,234,345,-999, 344,343,343]

new_temps = [temp/10 for temp in temps if temp != -999]      # it ignore when temp =-999
print(new_temps)


##if you want to make 0 if item is -999
new_temps_new = [item/10 if item !=-999 else 0 for item in temps]
print(new_temps_new)



