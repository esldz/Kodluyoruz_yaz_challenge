sayi = int(input("Sayı girin: "))
sayilar = []

for i in range(1, sayi + 1):
    if sayi % i == 0:
        sayilar.append(i)
        
print(f"{sayi} sayısının tam bölenleri toplamı {sum(sayilar)}")
