FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def digit_fact_sum(n):
    return sum([FACTORIALS[int(i)] for i in str(n)])

def count_matching_chains(upper, uniqueCount):
    chains = gen_fact_chains(upper)
    count = 0
    for i in range(upper):
        if i in chains and chains[i] == uniqueCount:
            count += 1
    return count

def gen_fact_chains(n):
    # the number of unique numbers that are generated from n
    # e.g. self loop = 1
    # dictionary so we can go above the bound of our array
    # without extra effort (e.g. digitFactSum(999999) > 2 million)
    chainlens = {}
    # simplify recursive code since we know all >1 loops ahead of time
    chainlens[169] = 3
    chainlens[363601] = 3
    chainlens[1454] = 3
    chainlens[871] = 2
    chainlens[45361] = 2
    chainlens[872] = 2
    chainlens[45362] = 872
    for i in range(n):
        gen_fact_chain_rec(i, chainlens)
    return chainlens

def gen_fact_chain_rec(i, chainlens):
    if i in chainlens:
        return
    nextI = digit_fact_sum(i)
    if i == nextI:
        chainlens[i] = 1
        return
    gen_fact_chain_rec(nextI, chainlens)
    chainlens[i] = 1 + chainlens[nextI]

print(count_matching_chains(10 ** 6, 60))
