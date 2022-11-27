import time
import random
import os
from termcolor import colored,cprint #py -m pip install termcolor


def alege_cuvant():
    f=open('cuvinte.in','r')
    g=open('cuvinte_posibile.in','w')
    cuv=f.readlines()
    for i in cuv:
        g.write(i)
    cu=random.choice(cuv)
    f.close()
    g.close()
    return cu

cuvant=alege_cuvant()


def cuvant_comun():
    #numarul de aparitii al unei litere
    f=open("cuvinte_posibile.in","r")
    counter=[0 for i in range(0,26)]

    for i in f:
        cuv=i
        for j in cuv:
            if 'A'<=j<='Z':
                counter[ord(j)-ord('A')]+=1

    f.close()

    nrlitere=sum(counter) #numarul de litere
    #frecventa literei
    frecventalit=[0 for i in range(0,26)]
    for i in range(len(counter)):
        frecventalit[i]=counter[i]/nrlitere

    #cat de comun este un cuvant
    f=open("cuvinte_posibile.in","r")
    tot=[]
    scor=0.0
    for i in f:
        for j in i:
            if 'A'<=j<='Z':
                scor+=frecventalit[ord(j)-ord('A')]
        tot.append(scor)
        scor=0.0

    #cel mai comun cuvant
    for i in range(len(tot)):
        if tot[i]==max(tot):
            return i

def formare_lista(ghicite,stiute,error):
    global cuvantj
    ghicite=list(ghicite)
    stiute=list(stiute)
    error=list(error)
    lista=[]
    fisier_dictionar = open("cuvinte_posibile.in",'r')
    continut = fisier_dictionar.read()
    dictionar = continut.split()
    fisier_dictionar.close()
    for cuvant in dictionar:
        ok=0
        for i in range(len(cuvant)):
            if cuvant[i]!=ghicite[i] and ghicite[i]!='_':
                ok=1
                break
        if ok==0:
            lista.append(cuvant)
    c=[]
    for i in range(len(lista)):
        ok=0
        for j in lista[i]:
            if j in error:
                ok=1
                break
        if ok==1:
            c.append(i)
    for i in range(len(c)):
        del lista[c[i]-i]
    c=[]
    for i in range(len(lista)):
        ok=0
        cuv=lista[i]
        for j in range(len(cuv)):
            if (cuv[j] in stiute) and cuv[j]!=ghicite[j]:
                if  cuv[j]==cuvantj[j]:
                    ok=0
                    break
                else:
                    ok+=1
        if ok>=len(stiute):
            c.append(lista[i])
    
    lista=c
    

    for i in range(len(lista)):
        if lista[i]==cuvantj:
            del lista[i]
            break
    
    g=open('cuvinte_posibile.in','w')
    for i in lista:
        g.write(i)
        g.write("\n")

def citeste():
    global cuvantj
    f=open("cuvinte_posibile.in","r")
    cuv=f.readlines()
    i=cuvant_comun()
    cuvantj=cuv[i]
    cuvantj=list(cuvantj)
    del cuvantj[-1]
    cuvantj=''.join(cuvantj)
    print("Cuvantul ales de bot este:",cuvantj)
    #time.sleep(3)

cuvantj= "a"


ghiceala=['_' for x in range(5)]
afis=[]
pont=[]
nu=[]
ok=0
nr=0

def joc():
    cuvant=alege_cuvant()
    cuvant=list(cuvant)
    del cuvant[-1]
    print(cuvant)
    global cuvantj,ghiceala,afis,nr,ok,pont,nu
    nr=0
    while ok!=1:
        formare_lista(ghiceala,pont,nu)
        citeste()
        
        nr+=1
        pont=[]
        nu=[]
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
                    if cuvant[j] not in pont:
                        pont.extend(cuvant[j])
                    ok=1
                    color[i]=colored(cuvantj[i],'yellow')
                    break
            if ok==0 and ghiceala[i]=='_':
                try:
                    ghiceala.index(cuvantj[i])
                except ValueError:
                    nu.extend(cuvantj[i])
            else:
                ok=0

        #os.system('cls')
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

            #print("Literele pe care le-ai ghicit sunt:",ghiceala)
            for i in range(len(afis)):
                print(afis[i])
            #print("Cuvantu scris de mine:",cuvantj)
            #print("Litere care au aparut in cuvant, dar nu sunt pe pozitia buna:",pont)
            #print("Literele care nu apar:",nu)
            #time.sleep(1)
    ok=0
    ghiceala=['_' for x in range(5)]
    afis=[]
    #os.system('cls')
    print("Felicitari, ai ghicit cuvantul din",nr,"incercari, iar cuvantul era",cuvant,".")
    
    
   

f=open("cuvinte.in","r")
cuv=f.readlines()
medie=[]
lista=[]

