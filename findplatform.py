
def findplatform(arrvl,dept,n):
    arrvl.sort()
    dept.sort()
     
    platform=1
    result=1
    i=1
    j=0

    while (i < n and j < n): 
     
        if (arrvl[i] < dept[j]): 
            platform+=1
            i+=1
            if (platform > result):  
                result = platform 
        else:
            platform-=1
            j+=1
          
    return result 
arrvl = [ 900, 915, 1030, 1045] 
dept = [ 930, 1300, 1100, 1145] 
n = len(arrvl)
print("Minimum Number of Platforms Required = ",findplatform(arrvl,dept,n))
