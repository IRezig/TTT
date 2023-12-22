from typing import TypeVar

T = TypeVar("T")


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
