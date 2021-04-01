# This is used for Terninary condition

condition = True 

if condition :
    x =1
else :
    x =0
print (x)

x = 1 if condition else  0
print(x)
# This is used for Iterators 

names =['wayne','john','mark','Oliver']
index =0
for name in names :
    print (name,index)
    index +=1

for name,index in enumerate(names , start =1):
    print(index,name)

clubs = ['manutd','astonvilla','mancity','chelsea']


for name,club in zip(names,clubs):
    print(f'{names} below to {clubs}')
