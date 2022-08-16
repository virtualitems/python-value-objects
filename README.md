## About

Abstract base class for python value objects.

## Usage

Extend and implement the _is_valid_ method.

```
class Weight(ValueObject):
    def is_valid(self, value: int) -> bool:
        return isinstance(value, int) and value >= 0
```

Equality example:

```
o = Weight(10)
p = Weight(11)
q = Weight(11)

print('o ', o)
print('p ', p)
print('q ', q)
print('o == p ', o == p)
print('o == q ', o == q)
print('p == q ', p == q)
```
