
# fig03_02.py
"""Class average program with sentinel-controlled iteration"""

# initialization phase
total = 0 # sum if grades
grade_counter = 0 # number of grades entered

# processing phase
grade = int(input('Enter grade, -1 to end: ')) # get one grade

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))

# Termination phase
if grade != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')


