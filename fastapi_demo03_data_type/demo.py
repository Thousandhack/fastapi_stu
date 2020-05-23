from typing import List
from typing import Dict


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + "_" + last_name.title()
    return full_name


print(get_full_name("TH", "HSZ"))


def process_items(items: List[str]):
    for item in items:
        print(item)


process_items(items=[1, 2, 3])


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
