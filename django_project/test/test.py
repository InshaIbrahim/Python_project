class myclass:
    
    a=10
    b=15
    def myfun(self):
        
        self.a = a
        self.b = b
        if(self.a == self.b):
            print ("these numbers are equal")
        else:
            print("these nubmers are not equal") 
            
obj = myclass()
obj.myfun            