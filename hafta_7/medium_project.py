sayilar = [4, 2, 5, 6, 9, 4, 4, 17, 4, 5, 7, 27, 4, 4, 78, 4]
sayilar.sort()  

n = len(sayilar)
if n % 2 == 1:
    medyan = sayilar[n // 2]
else:
    medyan = (sayilar[(n - 1) // 2] + sayilar[n // 2]) / 2

print(f"sayilar dizisinin medyanı = {medyan}")
