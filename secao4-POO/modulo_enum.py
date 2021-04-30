from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    for direction in Directions:
        print(direction, direction.value, direction.name)

# Sempre que você tiver algum set (conjunto pré-definido de escolhas) opte por utilizar o Enum, pois na validação fica bem mais fácil de evitar valores indesejados nos inputs.

# Uma enumeração é um conjunto de nomes simbólicos (membros) vinculados a valores únicos e constantes. Dentro de uma enumeração, os membros podem ser comparados por identidade, e a enumeração em si pode ser iterada.
