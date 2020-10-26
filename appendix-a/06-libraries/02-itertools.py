from itertools import permutations

# permutation
data = ['A', 'B', 'C']

result = list(permutations(data, 3))

print(result)

from itertools import combinations
# combination
result = list(combinations(data, 2))

print(result)

from itertools import product
# product
result = list(product(data, repeat = 2))

print(result)

from itertools import combinations_with_replacement
# combination with replacement
result = list(combinations_with_replacement(data, 2))

print(result)
