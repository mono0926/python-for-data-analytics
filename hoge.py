# generic List, supports indexing.
from typing import List, Optional

# In this case, the type is easily inferred as type: int.
i = 0

# Even though the type can be inferred as of type list
# there is no way to know the contents of this list.
# By using type: List[str] we indicate we want to use a list of strings.
a = []  # type: List[str]

# Appending an int to our list
# is statically not correct.
a.append(i)

# Appending a string is fine.
a.append("i")

print(a)  # [0, 'i']


def hoge(vvvvvv: str=None) -> str:
    vvvvvv.
    print(v + 2)
    return 1

hoge(1)