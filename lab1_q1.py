"""1)Given a collection of integers that might contain 
duplicates, nums, return all possible subsets. Do not include null subset"""

#Calling Sublist function
def sublist(inp_list):
    list1=[]
    n=len(inp_list)
    for i in range(2**n):
        subset=[]
        for j in range(n):
            if (i&(1<<j))!=0:
                subset.append(inp_list[j])
        if subset not in list1:
            list1.append(subset)
    return list1[1:]
    
#Give Input list
input_list=[1,2,2]
print(sublist(input_list))