from collections import defaultdict
from math import sqrt

def xs(p):
    return [x for x in range(2, int(sqrt(p)) + 1) if
            p % x == 0 and x + p/x <= 100 and x != p/x]

# For every sum calculate the producs that can only be factored in one way.

sums_to_products = {}
for s in range(5, 101):
    known = False
    maybe = set()
    for x in range(2, s):
        y = s - x
        if x < y:
            p = x * y
            maybe.add(p)
            if len(xs(p)) == 1:
                known = True
                break
    if not known:
        sums_to_products[s] = maybe

# Map these select products back to the sums that generated them.

products_to_sums = defaultdict(list)
for k, v in sums_to_products.items():
    for p in v:
        products_to_sums[p].append(k)

# Select only the products that map to unique generating sums.

products_to_unique_sums = {}
for k, v in list(products_to_sums.items()):
    if len(v) == 1:
        products_to_unique_sums[k] = v[0]

# Map the special sums to lists of products.

sums_to_products_again = defaultdict(list)
for k, v in list(products_to_unique_sums.items()):
    sums_to_products_again[v].append(k)

# Select only those sums that map to unique products.

sums_to_unique_products = []
for k, v in list(sums_to_products_again.items()):
    if len(v) == 1:
        sums_to_unique_products.append((k, v[0]))

# If we have a unique solution, find x and y satisfying s and p.

if len(sums_to_unique_products) == 1:
    s, p = sums_to_unique_products[0]
    for x in range(2, s):
        y = s - x
        if x < y:
            q = x * y
            if q == p:
                print(x,y)
