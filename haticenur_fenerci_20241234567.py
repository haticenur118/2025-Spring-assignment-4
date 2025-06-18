import numpy as np

# Each row: [ID, Math, Physics, Chemistry, Selective]
table = np.array([
    [125, 85, 90, 78, 92],
    [622, 72, 88, 91, 30],
    [309, 93, 87, 80, 60],
    [439, 65, 70, 75, 57],
    [875, 78, 82, 84, 78]
])

def find_students(table, min_score):
    scores = table[:, 1:]  # take only exam scores (skip the ID)
    mask = np.any(scores >= min_score, axis=1)  # check if any score is high enough
    id_num = table[mask, 0].astype(np.int64)  # get IDs of matching students
    tot_std = np.int64(id_num.shape[0])  # how many students matched
    return id_num, tot_std

id_num, tot_std = find_students(table, 90)

print("IDs:", id_num)
print("Count:", tot_std)
