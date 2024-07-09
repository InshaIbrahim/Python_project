class myclass:
    
   
    def myfun(self, a,b):
        
        
        if(a == b):
            print ("these numbers are equal")
        else:
            print("these nubmers are not equal") 
        return a+b    
            
obj = myclass()
x=int(input("enter first number"))
y =int(input("enter second number"))
p=obj.myfun(x,y)
print(p) 
          