sayilar=[4,2,5,6,9,4,4,17,4,5,7,27,4,4,78,4]
cift_sayilar=[]

for i in sayilar:
    if i%2==0:
        cift_sayilar.append(i)

print(f"dizindeki çift sayıların toplamı= {sum(cift_sayilar)}")