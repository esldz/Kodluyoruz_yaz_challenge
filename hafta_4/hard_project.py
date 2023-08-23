sayilar=[4,2,5,6,9,4,4,17,4,5,7,27,4,4,78,4]

hedef_sayi=int(input("Hedef sayıyı girin: "))

sayac=0
for i in sayilar:
    if(hedef_sayi==i):
        sayac+=1

print(f"dizinin içine {sayac} tane {hedef_sayi} vardır.")

