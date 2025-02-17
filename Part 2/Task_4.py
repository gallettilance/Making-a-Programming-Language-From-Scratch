# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 10:32:07 2022

@author: Krish Nath
"""
class Neg:
    def __init__(self,p):
        self.p = p
        
    def __repr__(self):
        return "- ( " + repr(self.p) + " )"
    
    def simplify(self):
        simp = self.p.simplify()
        
        return Mul(Int(-1), simp).simplify()
    
    
class Pow:
    def __init__(self, p1, p2):
        self.p1 = p1
        
        self.p2 = p2
        
    def __repr__(self):
        if isinstance(self.p1, Pow)!=True and isinstance(self.p1, Int)!=True and isinstance(self.p1, X)!=True:            
            if isinstance(self.p2, Pow)!=True and isinstance(self.p2, Int)!=True and isinstance(self.p2, X)!=True:
                 return "( " + repr(self.p1) + " ) ^ ( " + repr(self.p2) + " )"
             
            return "( " + repr(self.p1) + " ) ^ " + repr(self.p2)
        if isinstance(self.p2, Pow)!=True  and isinstance(self.p2, Int)!=True and isinstance(self.p2, X)!=True:
            return repr(self.p1) + " ^ ( " + repr(self.p2) + " )"
        
        return repr(self.p1) + " ^ " + repr(self.p2)
    
    
    def simplify(self):
        simp1 = self.p1.simplify()
        
        simp2 = self.p2.simplify()
        
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            
            if simp1.i == 1:
                return Int(1)
            
            if isinstance(simp2, Int):
                return Int(simp1.i ** simp2.i)
            
            if isinstance(simp2, Pow):
                if isinstance(simp2.p1, Int):
                    return Pow(Int(simp1.i ** simp2.p1.i), simp2.p2.simplify())
                
                if isinstance(simp2.p2, Int):
                    return Pow(Int((simp1.i ** simp2.p2.i)), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(1)
            
            if simp2.i == 1:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i ** simp2.i)
            # Need to Review
            if isinstance(simp1, Pow):
                if isinstance(simp1.p1, Int):
                    return Pow(Int(simp1.p1.i ** simp2.i), simp2.p2.simplify())
                
                if isinstance(simp1.p2, Int):
                    return Pow(Int(simp1.p1.i**simp2.i), simp2.p1.simplify())
        return Pow(simp1, simp2)
    
    
    
    
class Error:
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return self.message
    
    def divby0(self):
        return 1/0 
    
    
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def simplify(self):
        return self


class Int:
    def __init__(self, i):
        self.i = int(i)

    def __repr__(self):
        return str(self.i)

    def simplify(self):
        return self


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Div):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
             
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        
        return repr(self.p1) + " * " + repr(self.p2)

    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            
            if simp1.i == 1:
                return simp2
            
            if isinstance(simp2, Int):
                return Int(simp1.i * simp2.i)
            
            if isinstance(simp2, Mul):
                if isinstance(simp2.p1, Int):
                    return Mul(Int(simp1.i * simp2.p1.i), simp2.p2.simplify())
                
                if isinstance(simp2.p2, Int):
                    return Mul(Int(simp1.i * simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Int(0)
            
            if simp2.i == 1:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i * simp2.i)
            
            if isinstance(simp1, Mul):
                if isinstance(simp1.p1, Int):
                    return Mul(Int(simp2.i * simp1.p1.i), simp2.p2.simplify())
                
                if isinstance(simp1.p2, Int):
                    return Mul(Int(simp2.i * simp1.p2.i), simp2.p1.simplify())
        return Mul(simp1, simp2)
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub) or isinstance(self.p1, Mul):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub) or isinstance(self.p2, Mul):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add)  or isinstance(self.p2, Sub)  or isinstance(self.p2, Mul):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        
        return repr(self.p1) + " / " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Int(0)
            
            if isinstance(simp2, Int):
                if simp2.i == 0:
                    return Error("Error:Dividing by 0")
                
                return Int(simp1.i / simp2.i)
            
            if isinstance(simp2, Div):
                if isinstance(simp2.p1, Int):
                    return Div(Int(simp1.i / simp2.p1.i), simp2.p2.simplify())
                
                if isinstance(simp2.p2, Int):
                    return Div(Int(simp1.i / simp2.p2.i), simp2.p1.simplify())
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return Error("Error:Dividing by 0")
                #return Int(0)
            
            if simp2.i == 1:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i / simp2.i)
            
            if isinstance(simp1, Div):
                if isinstance(simp1.p1, Int):
                    return Div(Int(simp2.i / simp1.p1.i), simp2.p2.simplify())
                
                if isinstance(simp1.p2, Int):
                    return Div(Int(simp2.i / simp1.p2.i), simp2.p1.simplify())
        return Div(simp1, simp2)
class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return simp2
            
            if isinstance(simp2, Int):
                return Int(simp1.i + simp2.i)
        
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i + simp2.i)
            
        return Add(simp1, simp2)
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    def simplify(self):
        simp1 = self.p1.simplify()
        simp2 = self.p2.simplify()
        if isinstance(simp1, Int):
            if simp1.i == 0:
                return Neg.simplify(simp2)
            
            if isinstance(simp2, Int):
                return Int(simp1.i - simp2.i)
        if isinstance(simp2, Int):
            if simp2.i == 0:
                return simp1
            
            if isinstance(simp1, Int):
                return Int(simp1.i - simp2.i)
        return Sub(simp1, simp2)

#poly = Sub( Add( Int(4), Int(3)), Add( X(), Div( Int(0), Add( Sub(X(), X()), Int(1)))))
# e1=Mul(Int(7),(Mul(X(),Mul(X(),X()))))
# e2=Mul(Int(2),Mul(Mul(X(),Mul(X(),X())),Mul(X(),X())))
# e3=Sub((Mul(Int(3),X())),Int(4))
# e4=Mul(Int(2),(Mul(X(),X())))                                                            
# poly2=Div(Add(e1,(Add(e2,e3))),e4)
#poly3=Sub(Int(2),Int(3))
#print(repr(poly))
#print(repr(poly.simplify()))
#poly4=Sub(Int(0),X())
poly5 = Div(Int(1), Int(0))
print(repr(poly5.simplify()))
