f=open('exmp.py','r')   #Εργασια 3
l=f.readlines()         #Αμα θελει input απο τον χρηστη αλλο ονομα τοτε :x=input(Dwse onoma arxeiou)/n f=open(x,'r')
f.close()
f=open('exmp.py','w')
for i in l:
    if '#' in i:
        nl=i.strip()
        if nl[0]!='#':#ελεγχος αν η γραμμη αρχιζει με -> #
            tmp=i.split('#')
            sq=tmp[0].count("'")#μετραμε τα μονα αυτακια στην γραμμη
            dq=tmp[0].count('"')#μετραμε τα διπλα αυτακια στην γραμμη
            if sq%2==1 or dq%2==1:
                print (i)
                f.write(i)
            else:
                print (i.split('#')[0])
                f.write(i.split('#')[0])
    else:
        print (i)
        f.write(i)
#Η αρχικη μου προσπαθεια για την ασκηση ηταν με την χρηση των regular expressions αλλα δεν εβρισκα τροπο για το
#κλεισμενο μεσα σε αυτακια
'''import re
x=input("Dwse to onoma tou arxeiou")
#Το αρχειο και το προγραμμα πρεπει να βρισκονται στο ιδιο directory
f=open(x,'r+')
w = f.read()
nf = re.sub(r'((?<!\'|\")#.*)', "", w)
f=open(x,'w')
f.write(nf)
f.close()'''
#Python 3.7.2