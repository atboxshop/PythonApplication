print('Convert from seconds to hours and minutes program')
seconds = int(input('Enter a number of seconds you want: '))
hours = seconds // 3600
minutes = seconds % 3600
if minutes == 60:
    print(hours,'hours \
    ',minutes // 60,'minutes \
    and 0 seconds')
if minutes < 60:
    print(hours,'hours \
   and',minutes, 'minutes')
if minutes > 60:
    print(hours,'hours \
    ',minutes // 60, 'minutes \
    and',minutes % 60,'seconds')



