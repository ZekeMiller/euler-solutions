# this is like a weird backtracker with terrible pruning but it works so yehaw

def make_num( lst ):
    outside = lst[:len(lst)//2:]
    inside = lst[len(lst)//2:]
    result = []
    start_i = outside.index( min(outside) )
    each_sum = None
    for delt in range(len(outside)):
        outside_i = ( start_i + delt ) % len(outside)
        outermost = outside[outside_i]
        middle = inside[outside_i]
        innermost = inside[(outside_i + 1) % len(inside)]
        total = sum((outermost, middle, innermost))
        if each_sum is None:
            each_sum = total
        elif total != each_sum:
            return -1
        result.extend([outermost, middle, innermost])
    return int("".join([str(x) for x in result]))


def five_backtracker( lst, i, best=0 ):
    if i >= len(lst):
        return make_num( lst )
    for v in range(1, 2*5 + 1):
        if v not in lst and ( v != 10 or i < 5 ):
            lst[i] = v
            result = five_backtracker( lst[:], i+1, best )
            if result is not None and result > best:
                best = result
    return best

def five_gon_ring_max():
    values = [ -1 for _ in range(2*5) ]
    return five_backtracker( values, 0 )


print( five_gon_ring_max() )
