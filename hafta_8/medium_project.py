sayi = int(input("Sayı giriniz: "))
basamaklar = [int(digit) for digit in str(sayi)]

toplam=0
for i in basamaklar:
    toplam+=i
print(f"{sayi} sayısının basamakları toplamı {toplam}")
