

# global variables are fine
values = { "2" : 2 , "3" : 3 , "4" : 4 , "5" : 5 , "6" : 6 , "7" : 7 , "8" : 8 ,
           "9" : 9 , "T" : 10, "J" : 11 , "Q" : 12 , "K" : 13 , "A" : 14 }
suits = { "C" : 1 , "D" : 2 , "H" : 3 , "S" : 4 }


def valueFirst( hand ):         # sorts hand by value, then by suit within value
    return sorted( sorted( hand, key = lambda card: card[1] ), key = lambda card: card[0] )


def suitFirst( hand ):          # sorts hand by suit, then by value within suit
    return sorted( sorted( hand, key = lambda card: card[0] ), key = lambda card: card[1] )


def tupledHand( hand ):         # converts hand as list of strings to hand as list of tuples
    return list( map( lambda card: ( values[ card[0] ], suits[ card[1] ] ), hand ) )


def uniqueSuits( hand ):        # returns number of unique suits in the hand
    return len( set( [ card[1] for card in hand ] ) )


def uniqueValues( hand ):       # returns number of unique values in the hand
    return len( set( [ card[0] for card in hand ] ) )


def countValues( hand ):        # returns map of value to count of that value
    cards = {}
    for card in hand:
        val = card[0]
        if val in cards:
            cards[ val ] += 1
        else:
            cards[ val ] = 1
    return cards


def countSuits( hand ):     # returns map of suit to count of that suit
    suits = {}
    for card in hand:
        suit = card[1]
        if suit in suits:
            suits[ suit ] += 1
        else:
            suits[ suit ] = 1
    return suits


def isConsecutive( hand ):  # returns True or False
    minVal = hand[0][0]
    # print( "consecutive check", minVal, hand )
    return [ card[0] - minVal for card in hand ] == [ i for i in range( 5 ) ]


def isRoyalFlush( hand ):  # returns True or False
    return uniqueSuits( hand ) == 1 and hand[0][0] == 10


def straightFlush( hand ):      # checks if suitCount is 1, then uses straight to check straight
    if uniqueSuits( hand ) == 1:
        return straight( hand )


def fourOfAKind( hand ):    # returns None or the value in a single element list
    values = countValues( hand )
    for value in list( values.keys() ):
        if values[ value ] == 4:
            return [value]


def fullHouse( hand ):      # returns None or a list of the larger value then the smaller
    vals = countValues( hand )
    if sorted( list( vals.values() ) ) == [2,3]:
        first = list( vals.keys() )[0]
        if vals[ first ] == 3:
            return list( vals.keys() )
        else:
            return list( values.keys() )[::-1]


def flush( hand ):          # returns None or a list of the values in descending order
    if uniqueSuits( hand ) == 1:
        return highCard( hand )


def straight( hand ):       # returns None or a list of the values in descending order
    if isConsecutive( hand ):
        return highCard( hand )


def threeOfAKind( hand ):   # returns None or the value in a single element list (tie impossible)
    vals = countValues( hand )
    for val in vals.keys():
        if vals[ val ] == 3:
            return [val]


def twoPairs( hand ):       # returns None or a list of the larger than the smaller value (then the remaining card value)
    vals = countValues( hand )
    pairs = []

    for val in vals.keys():
        if vals[ val ] == 2:
            pairs += [ val ]
        else:
            last = val

    if len( pairs ) == 2:
        return sorted( pairs, reverse = True ) + [last]


def onePair( hand ):        # returns None or the value of the pair and the rest of the values
    vals = countValues( hand )
    pairVal = None
    others = []
    for val in vals.keys():
        if vals[ val ] == 2:
            pairVal = val
        else:
            for i in range( val ):
                others += [ val ]
    if pairVal is not None:
        return [ pairVal ] + sorted( others, reverse = True )



def highCard( hand ):       # returns a list of the cards values in descending order
    return sorted( [ card[0] for card in hand ], reverse = True )


def rankHand( hand ):       # returns the rank and any extra information provided
    result = None

    if isRoyalFlush( hand ):
        print( "royal", hand )
        return 9, None

    result = straightFlush( hand )
    if result is not None:
        return 8, result

    result = fourOfAKind( hand )
    if result is not None:
        return 7, result

    result = fullHouse( hand )
    if result is not None:
        return 6, result

    result = flush( hand )
    if result is not None:
        return 5, result

    result = straight( hand )
    if result is not None:
        return 4, result

    result = threeOfAKind( hand )
    if result is not None:
        return 3, result

    result = twoPairs( hand )
    if result is not None:
        return 2, result

    result = onePair( hand )
    if result is not None:
        return 1, result

    return 0, highCard( hand )



def compare( hand1, hand2 ):    # True if hand1 wins
    rank1, result1 = rankHand( hand1 )
    rank2, result2 = rankHand( hand2 )

    if not rank1 == rank2:
        return rank1 > rank2

    for i in range( len( result1 ) ):
        if not result1[i] == result2[i]:
            return result1[i] > result2[i]

    # should never reach
    print( "Tie detected" )
    print( hand1, hand2 )


def countWins( filename ):
    count = 0
    with open( filename ) as file:
        for line in file:
            stringHands = line.split( " " )
            hand1 = valueFirst( tupledHand( stringHands[:5] ) )
            hand2 = valueFirst( tupledHand( stringHands[5:] ) )
            if compare( hand1, hand2 ):
                count += 1

    return count


def main():

    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "p054_poker.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    print( countWins( abs_file_path ) )


main()

