"""
Module that provides a value object abstraction for model data objects.

* ValueObject   Value object abstraction.
* ImmutabeValue Named tuple with a single value.
"""

# syntax
from __future__ import annotations

# abstractions
from abc import ABC, abstractmethod

# dependencies
from collections import namedtuple


# Named tuple with a single value.
# This is used to make the value object immutable.
ImmutabeValue = namedtuple('ImmutabeValue', ('value',))


class ValueObject(ABC, ImmutabeValue):
    """
    Represents a entity whose value is its identity.
    """
    @abstractmethod
    def is_valid(self, value) -> bool:
        """
        Checks if the value is valid for this value object.
        """

    def __init__(self, value):

        if not self.is_valid(value):
            raise ValueError(
                f'not valid value for {self.__class__} value object')

        super().__init__()

    def __str__(self) -> str:
        return str(self.value)
