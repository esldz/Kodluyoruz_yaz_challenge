sayi = int(input("Sayı giriniz: "))
sayi_str = str(sayi)
rakamlar = list(sayi_str)
toplam = 0

for rakam in rakamlar:
    toplam += int(rakam) ** 3

if toplam == sayi:
    print(f"{sayi} sayısı Armstrong sayısıdır.")
else:
    print(f"{sayi} sayısı Armstrong sayısı değildir.")
