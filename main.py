# Dice sum probability calculator
# Författare: Alfred Kållberg
# Datum: 21-08-2024

def main():

    user_input = input()
    first_die = int(user_input.split(" ")[0])
    second_die = int(user_input.split(" ")[1])
    sums = {}

    for i in range(1, first_die + 1):
        for j in range(1, second_die +1):
            if i+j in sums:
                sums[i+j] += 1
            else:
                sums[i+j] = 1
    max_value = max(sums.values())
    for i in sums:
        if sums[i] == max_value:
            print(i)

if __name__ == "__main__":
    main()