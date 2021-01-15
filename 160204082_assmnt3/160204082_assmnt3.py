# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:07:27 2020

@author: Md. Zahid Fesabelilla
"""

f1 = open("file.txt", "r")
f2 = open("s1File.txt", "w")

b = "["

symbolTable = {}
lst = []

for line in f1:
   for word in line.split():
       if(word == "[kw" or word =="[op" or word =="[num" or word =="[sep" or word =="[par" or word =="[brc"):
        print(b,end = "",file=f2)
       elif(word != "[kw" and word != "[op" and word != "[num" and word != "[sep" and word != "[par" and word != "[brc"):
           print(str(word),end =" ",file=f2)
              
f1.close
f2.close

'''
f2 = open("s1File.txt", "r")
for line in f2:
   for word in line.split():
     print(word)

f2.close
'''
f2 = open("s1File.txt", "r")
print("Step-1 : ")
for line in f2:
    print(line)
    
f2.close


f2 = open("s1File.txt", "r")
for line in f2:
   for word in line.split():
       lst.append(word)
#print(word)

f2.close
print("\n")
print("Print List : \n", lst)
print("\n")
#print(len(lst))
f = 0
i = 0
fn = []
var = []
k = 0

innerFnVar = []

#create function list and veriable list
#print("----------------------------------")
for x in range(len(lst)):
    if(f == 0 and lst[x] == "[float]" or lst[x] == "[int]" or lst[x] == "[double]"):
        #print(lst[x])
        a = lst[x]
        f = 1
        flag = 1
        
    elif(f == 1 and lst[x] == "[id"):
        #print(lst[x])
        b = lst[x]
        f=2
    elif(f==2 and isinstance(lst[x],str)):
        #print(lst[x])
        c = lst[x]
        f = 3 
        #print(k)
        if(lst[x]=="f1]"):
            k = 1
    elif (k == 0 and f == 3 and lst[x]=="[(]"):
        #d = lst[x]
        fn.append(a)
        fn.append(b)
        fn.append(c)
        fn.append(lst[x])
        
        #symbolTable[i] = [fn]
        #k = 1
        f = 0
    elif (k == 1 and f == 3 and lst[x]=="[(]"):
        #d = lst[x]
        fn.append(a)
        fn.append(b)
        fn.append(c)
        fn.append(lst[x])
        #symbolTable[i] = [fn]
        k = 1
        f = 0
    elif(k == 1 and f == 3 and lst[x]=="[)]"):
          var.append(a)
          var.append(b)
          var.append(c)
          var.append("f")
          k = 1
          f = 0 
    elif (k == 1 and f == 3 and lst[x] == "[;]" ):
        e = lst[x]
        var.append(a)
        var.append(b)
        var.append(c)
        var.append("f")
        var.append(e)
        #print(lst[x])
        k = 0
        f = 0
        
    elif(lst[x] == "[}]"):
         k = 0
    elif (k == 0 and f == 3 and lst[x] == "[;]" ):
        e = lst[x]
        var.append(a)
        var.append(b)
        var.append(c)
        var.append(e)
        #print(lst[x])
        f = 0;
        
    elif(k == 0 and f == 3 and lst[x]=="[=]"):
        #print(lst[x])
        f=4
    elif(k == 0 and f == 4 and isinstance(lst[x],str)):
        #print(lst[x])
        d = lst[x]
        var.append(a)
        var.append(b)
        var.append(c)
        var.append(d)
        #symbolTable[i] = [var]
        f=5
        #f=0
    elif (k==0 and f == 5 and lst[x] == "[;]"):
        var.append(lst[x])
        f = 0
        s = 0
        print()
        
print("Print Only Function : \n",fn)
print("\n")
print("Print Only Veriable : \n",var)
print("\n")

# clean function list

cleanFn = []

only_alpha = ""
only_alpha1 = ""
#print("\n")
for i in range(len(fn)):
    string1 = fn[i]
    if(string1 == "[float]" or string1 == "[int]" or string1 == "[double]" ):
        for char in string1:
            if (char.isalpha()):
                only_alpha1 += char
        cleanFn.append(only_alpha1)
        only_alpha1 = ""        
        
    if(fn[i] == "[id" and fn[i] != '[(]'):
        string = fn[i+1]
        for char in string:#removing f1] to f1
            if (char.isalpha() or char.isnumeric()):
                only_alpha += char
        #print(only_alpha)
        cleanFn.append(only_alpha)
        cleanFn.append(".")
        only_alpha = ""
        
print("Print Clean Function : \n",cleanFn)
print("\n")

#clean veriable list

only_alpha2 = ""
cleanVar = []
findFnV = ""

for i in range(len(var)):
     string1 = var[i]
     if(string1 == "[float]" or string1 == "[int]" or string1 == "[double]" ):
        for char in string1:
            if (char.isalpha()):
                only_alpha1 += char
        cleanVar.append(only_alpha1); 
        only_alpha1 = ""        
        
     if(var[i] == "[id" and var[i] != '[;]'):
        j = i+1
        string = var[j]
        for char in string:
            if (char.isalpha() or char.isnumeric()):
                only_alpha += char
                
        if(isinstance(var[j+1],str) and var[j]!='[;]'):
            for char in str(var[j+1]):
                if (char.isnumeric() or char == "."):
                    only_alpha2 += char
        if(var[j+1] == "f"):
            findFnV = "f"
        
        #else:       
        #print(only_alpha)
        cleanVar.append(only_alpha)
        if(len(findFnV) == 1):
            cleanVar.append(findFnV)
            findFnV = ""
        if(len(only_alpha2) !=0):
            cleanVar.append(only_alpha2)
        cleanVar.append(";")
        only_alpha = ""
        only_alpha2 = ""

print("Print Clean Veriable : \n",cleanVar)

print("\n")
print("Symbol Table:  \n")
print("SL.No  DataType NameID  Value    Type   Scope")
print("----------------------------------------------")

z = int(1)
#finalFn = [];
finalF1 = ""

#only function print
for n in range(len(cleanFn)):
    if((cleanFn[n] == "float" or cleanFn[n] == "int" or cleanFn[n] == "double" )):
        finalF1 = str(z)+". \t" + cleanFn[n] 
    elif(cleanFn[n] != "."):
            finalF1 = finalF1+" \t"+ cleanFn[n] + "\t\t func"+"\tglobal"+"\t "
            z = z+1        
    elif(cleanFn[n] == "."):
        print(finalF1)
        finalF1 = " "

i = 0   
key = ""    
#only veriable print 
finalVar1 = ""      
for n in range(len(cleanVar)):
    if((cleanVar[n] == "float" or cleanVar[n] == "int" or cleanVar[n] == "double" )):
        finalVar1 = str(z)+". \t" + cleanVar[n] 
    elif(cleanVar[n] != ";"):
        if(cleanVar[n] == "f"):
            finalVar1 = finalVar1+"\t"+ key;
            key = "f"
        else:
            finalVar1 = finalVar1 +"\t"+cleanVar[n]
    else:
        if(flag == 1):
            print(finalVar1+"\t"+" var"+"\t"+"global")
            flag = 2;
            finalVar1=""
            z = z+1
        elif(key == "f"):
            print(finalVar1+"\t"+" var"+"\t"+"f1")
            key = ""
            z = z+1
        else:
            print(finalVar1+"\t\t"+" var"+"\t"+"main")
            finalVar1=""
            z = z+1
    
        
        




