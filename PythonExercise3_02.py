
# fig03_02.py
"""Class average program with sentinel-controlled iteration"""

# initialization phase
total = 0 # sum if grades
grade_counter = 0 # number of grades entered

# processing phase
grade = int(input('Enter grade, 0 to end: ')) # get one grade

if grade <= -1:
    print('No grades were entered,', 
          'grade must be equal or greater than 0')
else:
    while grade != -1:
        total += grade
        grade_counter += 1
        grade = int(input('Enter grade, 0 to end: '))
        if grade == -1:
            grade = -1
        elif grade < 0:
            print('Grade value must be run from 0 to end')
            grade = 0
            grade_counter -= 1

    if grade != 0: #Termination proccess
        average = total / grade_counter
        print(f'Class average is {average:.2f}')


