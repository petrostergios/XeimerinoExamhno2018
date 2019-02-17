f=open('exmp.txt',"r")   #Εργασια 12
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphaCount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
w=f.read().upper()
na=[]
nac=[]
for i in w:
    for ch in i:
        for j in range(len(alpha)):
            if ch == alpha[j]:
                alphaCount[j] += 1
for i in range(len(alpha)):
    print('The letter',alpha[i],'can be found',alphaCount[i],'times')
p=0
for i in range(len(alpha)):
    if alphaCount[i]!=0:
        na.append(alpha[p])
        nac.append(alphaCount[p])
    p += 1
#print(na)
#print(nac)
n=len(na)
for j in range(n):#Βαζω σε σειρα απο τα λιγοτερο εμφανιζομενα στα περισσοτερο εμφανιζομενα γραμματα σε μια λιστα(na)
    for k in range(0,n-j-1):
        if nac[k]>nac[k+1]:
            nac[k],nac[k+1]=nac[k+1],nac[k]
            na[k], na[k + 1] = na[k + 1], na[k]
#print(na)
#print(nac)
#print(w)
for i in range(int(n/2)):   #!!!! Αμα θελετε να γινει αλλαγη μονο των ακρων της λιστας απλα τρεξτε τις παρακατω γραμμες
    if nac[i]!=nac[-i -1]: # Εδω γινεται η ανταλλαγη των γραμματων                  #w = w.replace(na[0], '#$%')
        w = w.replace(na[i], '#$%')                                                 #w = w.replace(na[ - 1], na[0])
        w = w.replace(na[-i - 1], na[i])                                            #w = w.replace('#$%', na[- 1])
        w = w.replace('#$%', na[-i - 1])
print(w)
f.close()
#Python 3.7.2