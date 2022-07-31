## About

Abstract base class for python value objects.

## Usage

Extends and implement the _is_valid_ method.

```
class Weight(ValueObject):
    def is_valid(self, value: int) -> bool:
        return value >= 0
```

Equality example:

```
o = Weight(10)
p = Weight(11)
q = Weight(11)

print(o == p, o == q, p == q)
```
