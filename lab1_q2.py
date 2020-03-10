def concate(dict1, dict2): 
    result_dict = {**dict1, **dict2} 
    return result_dict 
      
# Driver code 
dict1 = {'p': 8, 'r': 5} 
dict2 = {'q': 2, 's': 9} 
dict3 = concate(dict1, dict2) 
print(dict3) 

for key, value in sorted(dict3.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
