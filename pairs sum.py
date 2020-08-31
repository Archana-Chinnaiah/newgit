value="RGBGBR"
count=0
list1=list(value)
for i in range (6):
    for j in range(i):
        if(list1[i] == list1[j]):
            print(list1[j])
        else:
            count = 0
if(count == 1):
    print("True")
else:
    print("False")
