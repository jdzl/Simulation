"""
@Cm
@param seed
@param Maxgenerator  { generator n numbers random}
@return {array with N elements random }
"""
import numpy as np

def Cm(Maxgenerator=1):
    nums= []
    Xn = 7
    a = 7
    c = 1
    m = 16547
    
    
    for iterator in range(Maxgenerator):        
        Xn_1 = (a*Xn + c)% m        
        out = float(Xn_1)/float(m)    
        nums.append(out)
        Xn = Xn_1
    return nums


