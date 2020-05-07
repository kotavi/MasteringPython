from enum import Enum


class AnimalEnum(Enum):
    HORSE = 1
    COW = 2
    CHICKEN = 3
    DOG = 4


for animal in AnimalEnum:
    print(repr(animal))

print(AnimalEnum.HORSE == 1)


class AnimalEnumStr(str, Enum):
    HORSE = 'horse'
    COW = 'cow'
    CHICKEN = 'chicken'
    DOG = 'dog'


print(AnimalEnumStr.HORSE == 'horse')

h = AnimalEnumStr.HORSE
print(h.value)
print(h.name)
