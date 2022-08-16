from __future__ import annotations
from typing import Any

from abc import ABC, abstractmethod

class ValueObject(ABC):
    _value: Any

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        raise Exception('cannot set value of immutable value object')

    def __init__(self, value: Any):
        if not self.is_valid(value):
            raise ValueError('not valid value for this value object')
        self._value = value

    def __eq__(self, other: ValueObject) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value

    def __str__(self) -> str:
        return str(self.value)

    @abstractmethod
    def is_valid(self, value) -> bool:
        pass
