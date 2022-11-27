import time
import random
import os
from termcolor import colored #py -m pip install termcolor


def alege_cuvant():
    f=open('cuvinte.in','r')
    cuv=f.readlines()
    cu=random.choice(cuv)
    f.close()
    return cu




def citeste():
    global cuvantj
    cuvantj= "a"
    while len(cuvantj)!=5:
        cuvantj=str(input("Ghiceste cuvantul(acesta are 5 litere):"))

        if len(cuvantj)!=5:
            print(cuvantj,"nu are 5 litere")
            time.sleep(1)
            os.system('cls')
            cuvantj=list(cuvantj)

cuvantj= "a"


ghiceala=['_' for x in range(5)]
afis=[]
ok=0
nr=0
def joc():
    cuvant=alege_cuvant() 
    cuvant=list(cuvant)
    del cuvant[-1]
    
    global cuvantj,ghiceala,afis,nr,ok
    while ok!=1:
        citeste()
        nr+=1
        pont=[]
        cuvantj=cuvantj.upper()
        color=list(cuvantj)
        cuvant=list(cuvant)
        for i in range(len(cuvantj)):
            for j in range(len(cuvant)):
                if cuvantj[i]==cuvant[j] and i==j:
                    ghiceala[i]=cuvant[j]
                    color[i]=colored(ghiceala[i],'green')
                    break
        for i in range(len(cuvantj)):
            for j in range(len(cuvant)):
                if cuvantj[i]==cuvant[j] and i!=j and ghiceala[j]=='_' and ghiceala[i]=='_':
                    pont.extend(cuvant[j])
                    color[i]=colored(cuvantj[i],'yellow')
                    break
        os.system('cls')
        ghiceala=''.join(ghiceala)
        color=''.join(color)
        cuvant=''.join(cuvant)
        afis.append(color)
        #cuvant=''.join(cuvant)
        if cuvant==ghiceala:
            ok=1
        else:
            ok=0
            ghiceala=list(ghiceala)

            for i in range(len(afis)):
                print(afis[i])
            time.sleep(1)
    ok=0
    ghiceala=['_' for x in range(5)]
    afis=[]
    os.system('cls')
    print("Felicitari, ai ghicit cuvantul din",nr,"incercari, iar cuvantul era",cuvant,".")
    nr=0
    time.sleep(2)
    os.system('cls')
