# from more_itertools import divide //BLAISE
from itertools import (
    chain,
    product,
    batched,
    combinations,
    groupby,
    islice,
    pairwise,
    zip_longest,
    repeat,
    starmap,
)


# batched
def get_batches(lst, batch_size):
    for my_batch in batched(lst, batch_size):
        print(my_batch)


# product : Cartesian product
def get_product(lst, repeat):
    for my_product in product(lst, repeat=repeat):
        print(my_product)


def get_chain(*lst):
    for my_chain in chain(lst):
        print(my_chain)


def get_combinations(lst, r):
    # returns r length subsequences of elements from the input iterable.
    for my_combination in combinations(lst, r):
        print(my_combination)


def get_slice(lst, start, stop, step):
    for my_slice in islice(lst, start, stop, step):
        print(my_slice)


def get_groupby(lst, key):
    # make an iterator that returns consecutive keys and groups from the iterable.
    for my_groupby in groupby(lst, key):
        print(my_groupby)


def get_pairwise(lst):
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    for my_pairwise in pairwise(lst):
        print(my_pairwise)


# get_batches([1, 2, 3, 4, 5, 6, 7, 8], 3)
# get_product([1, 2, 3], 2)
# get_chain("Hello", "Hey", "Hi")
# get_combinations([1, 2, 3, 4, 5, 6, 7, 8], 3)
# get_slice([1, 2, 3, 4, 5, 6, 7, 8], 2, 6, 2)
# get_groupby([1, 2, 3, 4, 5, 6, 7, 8], lambda x: x % 2 == 0)
# get_pairwise([1, 2, 3, 4, 5, 6, 7, 8])
