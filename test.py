class A:
    def displayA(self):
        print("weelcome A")
        
class B(A):
    def displayB(self): 
        print("weelcome B")
        
        
class C(B):
    def displayC(self):
        print("welcome C") 
        
obj =C()

obj.displayA()        
                      