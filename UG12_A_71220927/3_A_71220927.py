a=int(input('Masukkan Pembatas : '))
b=int(input('Masukkan angka yang dilarang : '))
for i in range(a+1):
    if i==b:
        continue

    print(i, end=' ')