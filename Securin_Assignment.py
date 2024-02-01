import numpy as np


# Part - A
die_A = [1, 2, 3, 4, 5, 6]

die_B = [1, 2, 3, 4, 5, 6]
total_combinations = (len(die_A) * len(die_B))
print("1 A --- Total Combinations:", total_combinations)

die_faces = [1, 2, 3, 4, 5, 6]

combinations_matrix = np.zeros((6, 6), dtype=int)
print("1 B --- Combinations Distribution:")
for i in range(6):
    for j in range(6):
        combinations_matrix[i, j] = die_faces[i] + die_faces[j]
print(combinations_matrix)

die_faces = np.array([1, 2, 3, 4, 5, 6])

combinations_matrix = np.add.outer(die_faces, die_faces)

# Calculate and display probability of each sum for i in range(2, 13):

sum_count = np.count_nonzero(combinations_matrix == i)

probability = sum_count / total_combinations
print("1 C --- Probability of each sum:")
print(f"P(Sum={i}) = {probability:.2%}")


# Part-B 

# Part - B for sample test case:
def undoom_dice(Die_A, Die_B):
    # Initialize new dice
    N_die_A = []
    N_die_B = []

    # For each possible sum from 2 to 12
    for s in range(2, 13):
        count_original = 0
        for i in range(1, 7):
            for j in range(1, 7):
                if i + j == s:
                    count_original += 1
        if s <= 7:  
            for i in range(1, 5):  
                for j in range(1, 7):  
                    if i + j == s:
                        N_die_A.append(i)
                        N_die_B.append(j)
                        break
        else:
            index = 12 - s  # Index for symmetric sum
            N_die_A.append(N_die_A[index])
            N_die_B.append(N_die_B[index])

    return N_die_A, N_die_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Apply the transform function
N_die_A, N_die_B = undoom_dice(Die_A, Die_B)

# Output the new dice
print("N_die_A:", N_die_A)
print("N_die_B:", N_die_B)

