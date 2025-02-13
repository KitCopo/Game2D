import math

class Vector2: 
    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        self.x = x
        self.y = y

    def add(self, other: 'Vector2') -> None: 
        """ Adiciona um vetor (tupla) ao vetor atual. """
        self.x += other.x
        self.y += other.y

    def sub(self, other: tuple[int | float, int | float]) -> None: 
        """ Subtrai um vetor (tupla) do vetor atual. """
        self.x -= other[0]
        self.y -= other[1]

    def normalize(self) -> None: 
        """ Normaliza o vetor (faz com que seu tamanho seja 1). """
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude

    def magnitude(self) -> float:
        """ Retorna o comprimento (magnitude) do vetor. """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dot(self, other: tuple[int | float, int | float]) -> float:
        """ Retorna o produto escalar entre este vetor e outro. """
        return self.x * other[0] + self.y * other[1]

    def scale(self, factor: int | float) -> None:
        """ Multiplica o vetor por um fator escalar. """
        self.x *= factor
        self.y *= factor

    def copy(self) -> "Vector2":
        """ Retorna uma cópia deste vetor. """
        return Vector2(self.x, self.y)

    def __repr__(self) -> str:
        """ Representação do vetor como string. """
        return f"Vector2({self.x}, {self.y})"

    def __tuple__(self) -> tuple[int | float, int | float]:
        """ Retorna o vetor como uma tupla (x, y). """
        return (self.x, self.y)
