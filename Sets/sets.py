odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8 }
primes = {2, 3, 5, 7, 11}
a = frozenset([1, 2, 3, 4,])

new = odds.union(evens)
intersec = odds.intersection(primes)

print(a.remove())
