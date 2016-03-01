"""
@MidSquare
@param seed
@param Maxgenerator  { generator n numbers random}
@return {array with N elements random }
"""

def MidSquare(seed, Maxgenerator=1):

    nums= []
    seedCurrent = seed
    for iterator in range(Maxgenerator):

        if(len(seedCurrent)%2==0):

            n = int(seedCurrent)
            seed2 = n**2
            stringc =  str(seed2)
            if len(stringc)%2!=0:
                stringc = "0"+ stringc


            border = len(seedCurrent)/2

            seedNew = stringc[border:len(stringc)-border]            
            output = "0."+ seedNew
            nums.append(float(output))
            seedCurrent = seedNew
        else:
            print "error"
        

    return nums

def Cm(x0, Maxgenerator=1):
    nums= []
    Xn = int(x0)    
    
    a = 5
    c = 7
    m = 1277    
    
    for iterator in range(Maxgenerator):        
        Xn_1 = (a*Xn + c)% m
        nums.append(Xn_1)
        Xn = Xn_1
    return nums
