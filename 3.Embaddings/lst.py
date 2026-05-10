lst=['apple','milk','banana']
a,b=sorted(list(enumerate(lst)),key=lambda x:x[1])[-1]

print(a,b)