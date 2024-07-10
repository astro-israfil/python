from typing import Union
from typing import Optional

num: int = 10

name: str = "Israfil"

# print(num)
# print(name)

def add(a: int, b: int) -> int:
    return a + b

# print(add(10, 20))

def process(value: Union[str, int]) -> str:
    if isinstance(value, int):
        return f"Number {value}"
    else:
        return f"String {value}"
    
# print(process(10))
# print(process("10"))


def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello guest"
    return f"Hello {name}"

print(greet("Israfil"))
print(greet())