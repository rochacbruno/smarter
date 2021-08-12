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

## Smart `Result` Wrapper

Instead of calling error prone functions, wrap it in a `Result` object

```py
def this_fails(x):
    return x / 0

w = Result(this_fails, 5)  # instead of w = this_fails(5)

w.is_error() # True
w.is_ok() # False
w.exc # ZeroDivisionError
w.unwrap_or(5) # 5
w.unwrap_or_else(lambda: 5) # 5
w.and_then(lambda x: x + 1, 5) # Raises ZerodivisionError
w.unwrap() # Raises ZeroDivisionError
```

```py
def this_succeeds(x):
    return 1 + x

w = Result(this_succeeds, 5)  # Instead of w = this_succeeds(5)
w.is_error() # False
w.is_ok() # True
w.exc # None
w.unwrap_or(5) # 6
w.unwrap_or_else(lambda: 'default') # 6
w.and_then(lambda value, x: value * x, 5).unwrap() # 30
w.unwrap() # 6

def double_integer(x):
    return x * 2

result = (
  w.and_then(double_integer)  # 12
   .and_then(double_integer)  # 24
   .and_then(double_integer)  # 48
   .and_then(double_integer)  # 96
   .unwrap()
) # 96

w.ok() # 6
```

By default all exceptions are `wrapped` in a `Result` object but it is
possible to specify the exception type.

```py
person = {'name': 'John', 'age': '25'}
w = Result(person.__getitem__, 'city', suppress=KeyError)
w.is_error() # True
w.exc # KeyError
w.unwrap_or('Gotham') # 'Gotham'

# When exception type is specified, other exceptions are not wrapped
# raising the original exception eagerly/immediately.
w = Result(person.get, 'city', 'other', 'another', suppress=KeyError)
Traceback (most recent call last):
...
TypeError: get expected at most 2 arguments, got 3
```

However the above example is better covered by the smart `>> get` described below.

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
