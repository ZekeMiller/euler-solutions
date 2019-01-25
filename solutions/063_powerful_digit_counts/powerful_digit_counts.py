

# upper bound on bases is 10 exclusive, since 10^n has n+1 digits
# for example 10^3=1000 has 4 digits.  This pattern continues upward

# I don't know if there's a way to find a clear upper bound on powers
# but since there is an easy upper bound on bases we don't really need it
# since the bases are all less than 10, the number of digits gained by
# incrementing the power is at most 1, so if the power is greater than
# the length, the length can never catch back up

total = 0

for base in range( 1, 10 ):
    power = 1
    while True:
        leng = len( str( base ** power ) )
        if leng == power:
            total += 1
        if power > leng:
            break
        power += 1

print( total )
