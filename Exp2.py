Exp2. Write a Python program to store marks scored in subject “Fundamental of 
Data Structure” by N students in the class. Write functions to compute following: 
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test
d) Display mark with highest frequency
 
 
 
 
def accept_marks(a):
    n=int(input("Enter the strength of class: "))
    for i in range(n):
       while True: 
          x=input("Marks of student %d:"%(i+1))
          if(x=="AB"):
             x=-1
             break;
          x=int(x)
          if(x>=0 and x<=30):
             break;
          else:
             print("Enter the valid number!")
       a.append(x)
def display_marks(a):
    n=len(a)
    for i in range(n):
         if(a[i]==-1):
            print("Student %d is absent"%(i+1))
         elif(a[i]>=0 and a[i]<=30):
            print("Marks of Student is: %d "%a[i])
def average_score(a):
    n=len(a)
    count =0
    sum=0
    for i in range(n):
        if(a[i]>=0 and a[i]<=30):
            sum=sum+a[i]
            count=count+1
    avg=sum/count
    print("Average of %d Students who are present is: %f"%(count,avg))    
def max_min(a):
    max=-1
    min=31
    for i in range(len(a)):
        if(a[i]>max):
           max=a[i]
           index=i
        if(a[i]<min and a[i]!=-1):
           min=a[i]
    print("Maximum number is %d"%max)
    print("Minimum number is %d"%min)
def absent(a):
    s=0;
    for i in range(len(a)):
         if(a[i]==-1):
            s=s+1;
    print("Total absent students are: ",s)

def frequency(a):
   i=0
   x=0
   n=len(a)
   while(i<n):
      count=0
      for j in range(n):
         if(a[i]==a[j] and a[i]!=-1):
            count=count+1
      if(count>x):
         x=count
         index=i
      i=i+1
   print("The maximum frequency is of %d" %a[index])                                
def main():
    fds=[]
    accept_marks(fds)
    display_marks(fds)
    average_score(fds)
    max_min(fds)
    absent(fds)
    frequency(fds)
main()