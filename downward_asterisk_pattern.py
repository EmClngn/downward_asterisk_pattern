# make a downward pyramid pattern with only asterisks

# pseudo code

# ask user for the desired layers of the pattern
layers = int(input("What is your desired layer of the pyramid? "))

# make the normal number pattern
for outer in range(layers + 1):
    for inner in range(outer):
        print(outer, end = " ")
    print()
# write it so that it's only asterisks and it's downward