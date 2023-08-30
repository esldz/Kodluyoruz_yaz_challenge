total_animals = 36
total_legs = 100
solution_found = False

for num_chickens in range(total_animals + 1):
    num_sheep = total_animals - num_chickens
    if (2 * num_chickens + 4 * num_sheep) == total_legs:
        print("Tavuk sayısı:", num_chickens)
        print("Koyun sayısı:", num_sheep)
        solution_found = True
        break