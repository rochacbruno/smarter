# Smarter

[![codecov](https://codecov.io/gh/rochacbruno/smarter/branch/main/graph/badge.svg?token=I9ZGCFTQT9)](https://codecov.io/gh/rochacbruno/smarter)
[![CI](https://github.com/rochacbruno/smarter/actions/workflows/main.yml/badge.svg)](https://github.com/rochacbruno/smarter/actions/workflows/main.yml)

Some objects could be smarter

```bash
pip install smarter
```

## SmartList

### regular `list` operations

```py
from smarter import SmartList

colors = SmartList(['red', 'green', 'blue'])

colors.append('yellow')
colors.extend(['orange', 'purple'])
colors.insert(1, 'black')
colors.remove('black')
```

### smart `list` operations

```py
colors.first() # 'red'
colors.last() # 'purple'
colors.first_or(13) # 'red'
colors.last_or("default") # 'purple'

items = SmartList([])  # empty list
items.first_or(13) # 13
items.last_or("default") # 'default'

items = SmartList([None, "", [], 13])
items.first_not_null() # ""

items = SmartList([None, "", [], 13])
items.first_not_nullable() # 13
```

## Smart `get` operations

### Given the following objects

```py
person = {'name': 'John', 'age': 30}
colors = ['red', 'green', 'blue']
position = (1, 2, 6, 9)

class Person:
    name = "John"
```

### Ubiquitous `get` operations using `>>` operator 

```py
# On a `dict` gets by `key`
person >> get('name') # 'John'
person >> get('age') # 30
person >> get('city', default='Gotham') # Gotham

# On a `list` gets by `index`
colors >> get(0) # 'red'
colors >> get(1) # 'green'
colors >> get(2) # 'blue'
colors >> get(3) # None
colors >> get(4, "default") # 'default'

# On a `tuple` gets by `index`
position >> get(0) # 1
position >> get(1) # 2

# On a `class` gets by `attribute`
p = Person()
p >> get('name') # 'John'
p >> get('age', default=45) # 45
```
