"""
@Cm
@param seed
@param Maxgenerator  { generator n numbers random}
@return {array with N elements random }
"""
import numpy as np

def Cm(x0, pA,pC,pM,Maxgenerator=1):
    nums= []
    Xn = int(x0) 
    a = pA
    c = pC
    m = pM    
    
    for iterator in range(Maxgenerator):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        nums.append(out)
        Xn = Xn_1
    return nums


