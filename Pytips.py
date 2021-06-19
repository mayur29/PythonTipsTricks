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

a,b = (1,2)
print(a,b)

a,_ =(1,2)
print(a)

a,b,*c = (1,2,3,4,5)
print(f'{a} and {b} and {c}')


class Person():
    pass 

person = Person()
person.First = 'Wayne'
person.Second = 'Ronney'

print(person.First)
first_key = 'First'

setattr(person,'first_key','Wayne')
print(getattr(person,first_key))


new_list = [x for x in range(10)] #list comprehension
new_dict = {x:x+1 for x in range(10)} #dictionary comprehension
new_set = {x for x in range(10)} #set comprehension
new_gen = (x for x in range(10)) #generator comprehension
