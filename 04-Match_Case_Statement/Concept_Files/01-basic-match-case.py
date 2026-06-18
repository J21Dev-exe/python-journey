# Basic Day Match

day = int(input('Enter day(in number): '))

match day:
    case 1:                             # Monday
        print('Monday')
    case 2:                             # Tueday
        print('Tuesday')
    case 3:                             # Wednesday
        print('Wednesday')
    case 4:                             # Thursday
        print('Thursday')
    case 5:                             # Friday
        print('Friday')
    case 6:                             # Saturday
        print('Saturday')
    case 7:                             # Sunday
        print('Sunday')

match day:
    case 1 | 2 | 3 | 4 | 5:             # Weekday
        print('It is a Weekday')
    case _:                             # Weekend
        print('It is a Weekend')