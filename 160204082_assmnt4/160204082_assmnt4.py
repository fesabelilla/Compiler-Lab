# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:39:46 2020

@author: Asus
"""
# regex 
import re

print("---------------------------------------\n")
print("Print line number uFile \n")
print("---------------------------------------\n")

f1 = open("file.txt", "r")
f2 = open("uFile.txt", "w")

line_num = 0;
ver = []
ver1 = []

#line number
search_phrase = "\n"
for line in f1.readlines():
    line_num += 1
    if line.find(search_phrase) >= 0:
        print (str(line_num)+" "+str(line),end ="",file=f2)
f1.close
f2.close

f2 = open("uFile.txt", "r")
for line in f2:
     print(line)
f2.close


#comment remove

print("---------------------------------------\n")
print("Comment remove u1File :\n")
print("---------------------------------------\n")

f2 = open("uFile.txt", "r")
f3 = open("u1File.txt", "w")


for line in f2:
    s = line 
    x = re.sub(r'\s*/\*(.|\n)*?\*/\s*|/[^\n]*','\n', s, re.DOTALL).strip() 
    #leading whitespace, /*, any text and newline up until the first *\, then any whitespace after that. or single line comment
    print (str(x),end ="\n",file=f3)
f2.close
f3.close

f3 = open("u1File.txt", "r")
for line in f3:
     print(line)
f3.close

#remove extra space

print("---------------------------------------\n")
print("Remove extra space u2File:\n")
print("---------------------------------------\n")


f3 = open("u1File.txt", "r")
f4 = open("u2File.txt", "w")

for line in f3:
    x = re.sub('\s+',' ',line)
    print(str(x),end = "\n",file=f4)
   
f3.close
f4.close

f4 = open("u2File.txt", "r")
for line in f4:
     print(line)
f4.close


k = 0

#lexeme

print("---------------------------------------\n")
print("lexemes in u3File \n")
print("---------------------------------------\n")

f4 = open("u2File.txt", "r")
f5 = open("u3File.txt", "w")

for line in f4:
    txt = line
    #x = re.search(";", txt, re.IGNORECASE)
   # print(x)
    if((re.search(";", txt, re.IGNORECASE)) != None):
        y = re.sub(";", " ; ", txt)
        z = re.sub("\{", " { ", y)
        i = re.sub("\}", " } ", z)
        j = re.sub("\(", " ( ", i)
        k = re.sub("\)", " ) ", j)
        l = re.sub("\=", " = ", j)
        print(str(l),end = "\n",file=f5)
        
    elif((re.search("\(", txt, re.IGNORECASE)) != None):
        y = re.sub("\(", " ( ", txt)
        z = re.sub("\)", " ) ", y)
        i = re.sub(",", " , ", z)
        j = re.sub("<", " < ", i)
        print(str(j),end = "\n",file=f5)
    elif((re.search("\{", txt, re.IGNORECASE)) != None):
        y = re.sub("\{", " { ", txt)
        print(str(y),end = "\n",file=f5)
    else:
        print(txt,end = "\n",file=f5)
f4.close()
f5.close()

f5 = open("u3File.txt", "r")
for line in f5:
     print(line)
f5.close


# add id
print("---------------------------------------\n")
print("Add id u4File \n")
print("---------------------------------------\n")

f5 = open("u3File.txt", "r")
f6 = open("u4File.txt", "w")

lst = []

k = 0 

for line in f5:
   for word in line.split():
       #print(word)
       if(word == 'int' or word == 'float' or word == 'double'):
           b = word + " id "
           ver.append(word)
           print(str(b),end = "",file=f6)
           k = 1
       elif k == 1 :
           print(str(word),end =" ",file=f6)
           lst.append(word)
           k = 0
           ver.append(word)
           ver1.append(word)
       else :
           if(word in lst):
               c = " id " + word
               print(str(c),end =" ",file=f6)
           else:    
               print(str(word),end =" ",file=f6)


   print( str(),end ="\n",file=f6)   
 
        
f5.close
f6.close

#print(lst)

f6 = open("u4File.txt", "r")
for line in f6:
     print(line)
f6.close


print("---------------------------------------\n")
print("Error Checking \n")
print("---------------------------------------\n")

flag1 = 0
flag2 = 0
flag3 = 0
count1 = 0
count2 = 0
count3 = 0
lineNo = 0
lstIfElse = []
checkIfElse = 0
elseCount = 0
elseLineNo = 0
lstB = []
checkB = 0
b1Count = 0
b2Count = 0

f1 = 0
f2 = 0
f3 = 0
fcount = 0
flag3 = 0

f5 = open("u3File.txt", "r")
for line in f5:
   s = 0
   for word in line.split():
       if((word.isnumeric()) and s == 0):
           lineNo = word
           s = 1
        
       if(word == "for"):
           f1 = 1
       elif(f1 == 1 and word == "("):
           f2 = 1
       elif(word == ";" and f2 == 1):
           fcount = fcount + 1
           f3 = 1
           if(fcount > 2):
               flag3 = fcount
       elif(word == ")" and f3 == 1):
           f1 = 0
           f2 = 0
           f3 = 0
               
       if(word == ";" and f3 == 0):
           count1 = count1 + 1
           if(count1 >= 2):
               flag1 = count1
           #print(lineNo," ",count)
       elif(word != ";"):
           count1 = 0
#int           
       if(word == "int"):
           count2 = count2 + 1
           if(count2 >= 2):
               flag2 = count2
           #print(lineNo," ",count)
       elif(word != "int"):
           count2 = 0 
#for {}
       if(word == "{" or word =="}" ):
           lstB.append(lineNo)
           lstB.append(word)
#if else 
       if(word == 'if' or word == "else"):
           lstIfElse.append(lineNo)
           lstIfElse.append(word)

           
   if(flag1 >= 2):
       print("Duplicate token in line no ",lineNo)
       count1 = 0
       flag1 = 0
   if(flag3 > 2):
       print("Duplicate token in line no ",lineNo)
       fcount = 0
       flag3 = 0
   if(flag2 >= 2):
       print("Declaration error in line no ",lineNo)
       count2 = 0
       flag2 = 0

#print(lstIfElse)       
for i in range(len(lstIfElse)):
    if(lstIfElse[i] == 'if'):
         checkIfElse = 1
    elif(lstIfElse[i] == 'else' and checkIfElse==1):
         elseCount = elseCount + 1 
    if(elseCount == 2):
         print("Unmatched 'else' at line ", lstIfElse[i-1])
         checkIfElse = 0
         elseCount = 0
         #break;       

#print(lstB)
for i in range(len(lstB)):
    if(i%2 != 0):
        if(lstB[i] == "{"):
            checkB = 1;
            b1Count = b1Count + 1
        elif(lstB[i] == "}" and checkB == 1):
           # bCount = bCount + 1
           b2Count = b2Count + 1
           if(b1Count != b2Count):
             print("Misplaced '}' at line ", lstB[i-1])
             checkB = 0
             bCount = 0
             #break
 
f5.close


#print(ver)
#print(ver1)

# find undeclared identifiers
for i in range(len(ver1)):
    if ver1[i] not in ver :
        print("undeclared identifiers : ",ver1[i])   
        
    






























