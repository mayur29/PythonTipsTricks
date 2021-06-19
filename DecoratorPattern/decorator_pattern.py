
def Check(func):
    def validate(a,b):
        if b==0:
            print('B cant be zero')
            return 
        func(a,b)
    return validate

@Check
def divide( a,b) :
    print(a/b)

divide(2,0)