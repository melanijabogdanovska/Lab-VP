import random
number_list=[]
for i in range(10):
    number_list.append(i)
random.shuffle(number_list)
print(number_list)


for i in range(0,len(number_list),3):
    print(f" index: {i}")
    print(f" list: {number_list}")
    print(f" list_current_element: {number_list[i]}")
    print("  ")
    result=number_list[i]+number_list[1+i]
    number_list.insert(2+i,result)
print(number_list)
