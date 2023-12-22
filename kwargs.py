from typing import TypedDict, Unpack


class Movie(TypedDict):
    name: str
    year: int
    rating: float


def print_movie_info(**kwargs: Unpack[Movie]):
    print(f"Name: {kwargs['name']}")
    print(f"Year: {kwargs['year']}")
    print(f"Rating: {kwargs['rating']}")
