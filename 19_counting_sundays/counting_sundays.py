
days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def countSundays():

    sundays = 0
    day = 0

    for year in range( 1900, 2001 ):

        # check leap year
        leapYear = ( year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 ) )
            
        for month in range( 12 ):

            # check if day is val 6 ( sunday )
            if day == 6 and year > 1900:
                sundays += 1

            # adjust day
            if leapYear and month == 1:     # leapYear and it's February
                day = ( day + 1 ) % 7

            day = ( day + days[month] ) % 7

    return sundays



def main():
    print( countSundays() )


main()
