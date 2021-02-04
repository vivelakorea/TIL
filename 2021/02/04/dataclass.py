from dataclasses import dataclass


@dataclass
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.weight = 'a'
apple.price = 3.21

print(apple.weight)
