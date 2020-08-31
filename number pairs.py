list=[1,5,7,-1]
sum=6
count=0
print("pairs are")
for i in range(4):
     for j in range(i+1):
          if((list[i]+list[j])==sum):
               count=count+1
               print("(",list[i],",",list[j],")")
print(count)
                     
          
