
time_start = -1
first_try = True
while time_start not in range(25):
    if not first_try:
        print('\nTry again!')
    first_try = False
    time_start = int(input('Time [0-24]: '))

for i in range(0, 61):
    if i != 60:
        if len(str(i)) == 1:
            print(f'At {time_start}:0{i} or\n')
        else:
            print(f'At {time_start}:{i} or\n')
    else:
        print(f'At {time_start+1}:00')