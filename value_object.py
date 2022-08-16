"""
Value object abstraction.
"""

from __future__ import annotations
from typing import Any

from abc import ABC, abstractmethod


class ValueObject(ABC):
    """
    Represents a entity whose value is its identity.
    """
    _value: Any
    _initialized = False

    @abstractmethod
    def is_valid(self, value) -> bool:
        """
        Checks if the value is valid for this value object.
        """

    @property
    def value(self) -> Any:
        """
        Returns the value of this value object.
        """
        return self._value

    def __init__(self, value: Any):

        if not self.is_valid(value):
            raise ValueError('not valid value for this value object')

        self._value = value
        self._initialized = True

    def __setattr__(self, name, value) -> None:
        assert not self._initialized, 'Cannot set attributes on this class'
        super().__setattr__(name, value)

    def __delattr__(self, __name: str) -> None:
        assert False, 'Cannot delete attributes on this class'

    def __eq__(self, other: ValueObject) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._value == other._value

    def __ne__(self, other: ValueObject) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return str(self._value)
