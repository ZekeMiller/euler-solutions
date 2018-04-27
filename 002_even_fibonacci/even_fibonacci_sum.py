
prev2 = 0
prev = 1
num = 0

while ( prev + prev2 < 4000000 ):
    number = prev + prev2
    prev2 = prev
    prev = number
    if number % 2 == 0:
        num += number
print( num )
