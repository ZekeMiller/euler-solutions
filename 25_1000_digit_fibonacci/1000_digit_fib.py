
curr = 1
prev = 0
index = 1

while len(str(curr)) < 1000:
    new = curr + prev
    prev = curr
    curr = new
    index += 1

print( index )
