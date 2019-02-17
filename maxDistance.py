def maxDistance(x,y):   #Εργασια 13
    import itertools
    mikos = []
    sMikh = []
    for i in range(len(x)):
        mikos.append(x[i])
    #print(mikos)
    mikos.sort()
    #print(mikos)
    for i in range(len(x)):
        if y<mikos[i]:
            pos=i-1       #Μικαραινουμε το ευρος των επαναληψεων
            break
        else:
            pos=i
    #print(pos)
    for k in range(1,pos+1):
        for subset in itertools.combinations(mikos,k):
            #print(subset)
            o = 0
            for l in range(len(subset)):
                o+=subset[l]
            sMikh.append(o)  #Βαζω στην λιστα τα συνολικα μηκη (μοναδικος συνδυασμος των στοιχειων της λιστας καθε φορα)
    u=0
    for h in range(len(x)):
        u+=x[h]
    sMikh.append(u)
    #print(sMikh)
    sMikh.sort()
    #print(sMikh)
    for i in range(len(sMikh)):
        if y<sMikh[i]:
            pos=i-1       #Μικαραινουμε το ευρος των επαναληψεων
            break
        else:
            pos=i
    print(sMikh[pos])
maxDistance([50,166,99,150],360)
#Python 3.7.2