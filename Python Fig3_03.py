passes = 0
failures = 0

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail):'))

    if result == 1:
        passes += 1
    elif result == 2:
        failures += 1
    else:
        print('Result inputing must be either 1 or 2')

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

