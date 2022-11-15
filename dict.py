text=str(input(" Enter a text"))
recnik={}
print(text)
for item in text:
    print(item)
    if item in recnik:
        recnik[item]+=1
    else:
        recnik[item]=1
print(recnik)