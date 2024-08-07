
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('TIME OVER!')

while True:
    try:
        time_value = int(input('Enter the time in hours, minutes or seconds: '))
        break
    except ValueError:
        print('Invalid input. Please, enter a number.')

while True:
    time_unit = input('Is it in hours, minutes or seconds? \nEnter one of these options: h, m or s ').lower()
    if time_unit in ['h', 'm', 's']:
        break
    else:
        print('Invalid unit. Please, enter h, m, or s.')

if time_unit == 'h':
    t = time_value * 3600
elif time_unit == 'm':
    t = time_value * 60
elif time_unit == 's':
    t = time_value
else:
    print('Invalid unit. Please enter h, m, or s.')
    t = 0

if t > 0:
    countdown(t)
