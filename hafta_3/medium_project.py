total_animals = 36
total_legs = 100
solution_found = False

for num_chickens in range(total_animals + 1):
    num_sheep = total_animals - num_chickens
    if (2 * num_chickens + 4 * num_sheep) == total_legs:
        print(f"Tavuk sayısı: {num_chickens}\nKoyun sayısı: {num_sheep}" )
        solution_found = True
        break