import itertools


def print_batches(lst, batch_size):
    for batch in itertools.batched(lst, batch_size):
        print(batch)


print_batches([1, 2, 3, 4, 5, 6, 7, 8], 3)
