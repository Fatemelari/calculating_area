def circle():   #calculate the area of the circle
    r=int(input("enter the ray of the circle:"))   #getting radius
    s=r*r*3.14   #circle area formula
    print("the circle's area  by raduis",r,"is:",s)
    print("\n")
    return 

def square():   #calculate the area of the square
    n=int(input("enter the side of the square:"))   # getting the side size
    s=n*n        #square area formula
    print("the square's area by side siz",n,"is:",s)
    print("\n")
    return 

def triangle():   #calculate the area of the triangle
    x=int(input("enter the base of the triangle:"))   #getting the base of triangle
    y=int(input("enter the height of the triangle:")) #getting the height of the triangle
    s=x*y/2   #triangle area formula
    print("the triangle's area by base",x,"and  height",y,"is:",s)
    print("\n")
    return 

def rectangle():   #calculate the area of the rectangle
    a=int(input("enter the length of the rectangle:"))   #getting the length of the rectangle
    b=int(input("enter the width of the rectangle:"))    #getting the width of the rectangle
    s=a*b   #rectangle area formula
    print("the rectangle's area by length",a,"and width",b,"is:",s)
    print("\n")
    return 
def get_func():
    shape=[]
    x=input("enter type of shape:\n")
    shape.append(x)
    for i in range(0,3):
        y=input("")
        shape.append(y)
    print(shape)
    for i in range(len(shape)):
        if(shape[i]=="circle"):
            circle()
        elif(shape[i]=="square"):
            square()
        elif(shape[i]=="triangle"):
            triangle()
        elif(shape[i]=="rectangle"):
            rectangle()
        else:
             print("it's not define!")
            
    
sh=get_func()
