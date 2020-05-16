#NUMBER IS EVEN OR NOT

a=int(input("Enter the number:"))
if(a%2==0):
    print("number is even" ,a)
else:
    print("number is odd" ,a)   
    
    
    
   #NUMBER IS PRIME OR NOT 
    a=int(input("Enter the numbe:r"))
f=0
for i in range(2,a):
     if(a%i==0):
       f= 1
if(f==0):
     print("number is prime",a)
else:
     print("number is not prime",a
     
    #NUMBER IS PALLENDROMEOR NOT
  
  a=int(input("Enter the number:"))
rev=0
temp=a
while(temp>0):
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
if(a==rev):
    print("number is palindrome",a)
else:
    print("number is not palindrome",a)  
    
    
    
    #NUMBER IS ARMSTRONG OR NOT
    
a=int(input("Enter the number:"))
s=0
temp=a
while(temp>0):
    d=temp%10
    s+=d**3
    temp=temp//10
if(a==s):
    print("number is armstrong",a)
else:
   print("number is not armstrong",a) 
