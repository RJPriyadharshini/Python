# Number of rows for the pattern
num_rows = 5

# Upper half of the pattern
for i in range(num_rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(num_rows - 2, -1, -1):
    for j in range(i + 1):
        print("*", end=" ")
    print()







