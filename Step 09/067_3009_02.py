x=y=0
for i in range(3):
    exec("a,b=map(int,input().split());x=x^a;y=y^b;" * 3)
print(x,y)