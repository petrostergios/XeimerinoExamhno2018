def sumIntervals(x):   #Εργασια 1
    a=[]
    mikos=[]
    ari8moi=[]
    for i in range (len(x)):
        mikos.append(x[i][1]-x[i][0])
        #print(mikos)
        k=x[i][0]
        for j in range (mikos[i]+1):
            ari8moi.append(k)
            a.extend(ari8moi)
            k = k + 1
    a.sort()
    #pirnt(a)
    result = 0
    if type(a) == list:
        for i in range(len(a)):
            if a[i]-a[i-1]==1:
                result = result+1
    print(result, "einai to apotelesma")
sumIntervals([[10,18],[14,19]])
#Python 3.7.2