


def finde_pairs_for_numbers(target_number):
    pairs = []
    for i in range(1, target_number + 1):
        for j in range(i, target_number + 1):
            if ((i+j) % target_number == 0) and (i != j):
                pairs. append(f'{i}{j}')
    return pairs

for number in range(3, 21):
    numbers = finde_pairs_for_numbers(number)
    result = ''.join(map(str, numbers))
    print(f'{number}-{result}')

-------------------------------------------------
def finde_pair_for_numbers(target_number):
    pairs = []
    for i in range(1, target_number + 1):
        for j in range(i, target_number + 1):
            if ((i+j) % target_number ==0) and (i != j):
                print(f'{i}{j}')
    return pairs
for number in range(3,21):
    numbers = finde_pair_for_numbers(number)
    result = ''.join(map(str, numbers))
    print(f'{number}-{result}')