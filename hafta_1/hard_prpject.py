import random #random kütüphanesini yüklendi

#içinde tam sayılar olan dizi oluşturuldu
nums = [1, 3, 5, 7, 10, 15, 17, 19, 21, 22, 25, 28, 32, 35, 44, 53]
select_nums=[] #seçilen sayıları içine eklenecek boş bir dizi oluşturuldu.

hedef_sayi = int(input("Hedef sayıyı giriniz: ")) #kullanıcıdan hedef sayıyı girmesini istedik.

toplam = 0
sayac = 0

while toplam != hedef_sayi:
    select_num = random.choice(nums) #diziden rastgele bir sayı seçmesi istendi
    if toplam + select_num <= hedef_sayi:
        select_nums.append(select_num)
        toplam += select_num
        sayac += 1


print(f"Hedef sayıya {sayac} tam sayının toplamı ile ulaşıldı.")
print("Seçilen sayılar:", select_nums)