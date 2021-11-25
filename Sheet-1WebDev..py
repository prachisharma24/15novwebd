# Ques1. Explaination

#Ques2.
a=5**9
print(a)

a=3//2
print(a)

a=7//3
print(a)

a=7/3
print(a)

a=20;
a+=30;
a%=3;
print(a)

print(True*False)

print(True& False)

print(True and False)

print((6>3) and (7<4) or (18 == 3)) and (9>3)

print(True is False)

# print(False in 'False') # Type Error - Left Operator should be of <string>

print((True == False) or (False > True)) and (False <= True)

#Ques3.
s1 = "Nice to have it"
s2 = "here"
print(s1+' '+s2)  #print(s1,s2)

#Ques4.
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
k=a[3][1][2][0]
print(k)

#Ques5.
a.insert(0,s1)
a.append(s2)
print(a)

#Ques6.
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in numbers:
    if(i==237):
        break
    elif(i%2 == 0):
        print(i)

#The First number in the list is greater than 237 and hence no numbers get printed.

#Ques7.
        color_list_1 = set(["White","Black","Red"])
        color_list_2 = set(["Red","Green"])
        print(color_list_1-color_list_2)

#Ques8.
string = input("enter the string ")
string=  set (string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string :
    if (word in alpha):
        i+=1
if (i==26):
    print('string is pangram')
else :
    print('string is not pangram')


#Ques9.
n=(input("Enter a number - "))
num1=n
num2=n*2
num3=n*3
print(int(num1)+int(num2)+int(num3))

#Ques10.

#Qoes11.
string2=(input("enter the words"))
string2=string2.strip()
string2+=","
word=""
l=[]
for i in string2:
    if(i!=","):
        word+=i
    else:
        l.append(word)
        word=""
l.sort()
print(l)

#Ques12.

#ques13.
string3=(input("enter the sentence"))
letters=0
digits=0
for i in string3:
    if(i.isalpha()):
        letters+=1
    if(i.isdigit()):
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)

#Ques14.

#Ques15.
n = int(input())
divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print(divBy7)

#Ques 16.


       


