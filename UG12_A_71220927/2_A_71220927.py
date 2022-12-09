a=str(input('masukkan nama : '))
x=0
for i in range(len(a)):
    x=x+1
    print(a[:x])
        
for i in range(len(a)):
    x=x-1
    print(a[:x])
