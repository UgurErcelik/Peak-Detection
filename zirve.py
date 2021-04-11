# -*- coding: utf-8 -*-

#181307007 Uğur Erçelik

import numpy as np

def read_file(isim):
    
    liste = []
    
    
    f=open(isim, "r")
    if f.mode == 'r':
        liste = f.read()
        liste2 = liste.split('\n')
        return liste2
    
metin = read_file('mahalle.txt')
print("Metin : ",metin)

def string2matris(metin):
    
    matrix = []
    
    for row in metin:
        
        matrix.append([])
        
        for col in row:
            
            matrix[-1].append(col)
            
    return matrix


matris = string2matris(metin)
print("Matris : ",matris)

#Matris Konum : matris_np[i,j]
#Matrisin Kuzeyi : matris_np[i-1,j]
#Matrisin Doğusu : matris_np[i,j+1]
#Matrisin Güneyi : matris_np[i+1,j]
#Matrisin Batısı : matris_np[i,j-1]

matris_np = np.array(matris,dtype=object)
print("Yeni Matris :\n",matris_np)

max_rows = len(matris_np)
max_columns = len(matris_np[0])


print("Satır ve Sütun : ",max_rows,max_columns)

yList = []

print(" ")
print("----------Kısım 1----------")
print(" ")

for i in range(max_rows):
    
    for j in range(max_columns):
        
        
        if j-1 >= 0:
            batı = matris_np[i,j-1]
        else:
            batı = 0
            
        if j+1 < max_columns:
            dogu = matris_np[i,j+1]
        else:
            dogu = 0
            
        
        if i-1 >= 0:
            kuzey = matris_np[i-1,j]
        else:
            kuzey = 0
            
        
        if i+1 < max_rows:
            guney = matris_np[i+1,j]
        else:
            guney = 0
            
        
            
        if int(kuzey)+int(dogu)+int(guney)+int(batı) <= int(matris_np[i,j]):#Hepsi var
         
            print("Zirve : ",matris_np[i,j])
            yList.append(matris_np[i,j])
         


print(" ")
print("----------Kısım 2----------") 
print(" ")
      

print("Yeni Liste: " , yList)

maxNumber = yList[0]

for i in range(0,len(yList)):
    
    for j in range(0,len(yList)-1):
        
        if yList[j] < yList[j+1] :
            
            yList[j],yList[j+1]=yList[j+1],yList[j]
           
            
            
        else:
            continue
        
        if maxNumber < yList[i]:
            maxNumber = yList[i]
        
           
    
     
print("Sıralanmış Yeni Dizi  : ",yList)
print("Haritadaki En Zirve    : {0} ".format(maxNumber))

 
print(" ")
print("----------Kısım 3----------") 
print(" ")

maxNumber = yList[0]

def mergeSort(dizi):
    if len(dizi) > 1:
 
         
        mid = len(dizi)//2
 
        
        L = dizi[:mid]
 
       
        R = dizi[mid:]
 
        
        mergeSort(L)
 
       
        mergeSort(R)
 
        i = j = k = 0
 
        
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                dizi[k] = L[i]
                i += 1
            else:
                dizi[k] = R[j]
                j += 1
            k += 1
 
        
        while i < len(L):
            dizi[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            dizi[k] = R[j]
            j += 1
            k += 1
            
 
def ListeBastır(dizi):
    for i in range(len(dizi)):
        print(dizi[i], end=" ")
    print()
    
    
if maxNumber < yList[i]:
        maxNumber = yList[i]
 

print("Sıralanmış Yeni Dizi: ", end="\n")
ListeBastır(yList)
print("Haritadaki En Zirve: ",maxNumber)