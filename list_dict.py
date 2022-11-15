x=int(input(" Enter a num"))
a=[i for i in range (0,x)]
print(a)
recnik={}
for index in range(len(a)):
    recnik[index]=a[-1-index]
print(recnik)
