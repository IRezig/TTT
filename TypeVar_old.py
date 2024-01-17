from typing import TypeVar

# TypeVar is a special type of variable that works with Generics
# Generics are a way to make your code more reusable

T = TypeVar("T")  # Can be anything


def add(a: T, b: T) -> T:
    return a + b


print(add(1, 2))
print(add(1, 2.4))
print(add(1.3, 2.3))
print(add("Hello", "World"))


def first_element(lst: list[T]) -> T:
    return lst[0] if lst else None


print(first_element([1, 2, 3]))
print(first_element(["a", "b", "c"]))
print(first_element([]))
