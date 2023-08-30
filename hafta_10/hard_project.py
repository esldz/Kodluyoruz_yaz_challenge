from math import comb

total_students = 30
group_size = 4

different_ways = comb(total_students, group_size)
print(f"Öğrencilerden {group_size} kişi seçilebilecek farklı şekiller: {different_ways} farklı şekil")
