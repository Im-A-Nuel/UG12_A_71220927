x=int(input('Masukkan awal deret: '))
y=int(input('Masukkan akhir deret: '))
for i in range(x,y):
    if i%2==1 and i%6!=0 and i%3!=0:
        print(i, end=' ')