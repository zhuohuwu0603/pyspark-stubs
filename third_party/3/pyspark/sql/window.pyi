# Stubs for pyspark.sql.window (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Window:
    unboundedPreceding = ...  # type: Any
    unboundedFollowing = ...  # type: Any
    currentRow = ...  # type: int
    @staticmethod
    def partitionBy(*cols): ...
    @staticmethod
    def orderBy(*cols): ...
    @staticmethod
    def rowsBetween(start, end): ...
    @staticmethod
    def rangeBetween(start, end): ...

class WindowSpec:
    def __init__(self, jspec) -> None: ...
    def partitionBy(self, *cols): ...
    def orderBy(self, *cols): ...
    def rowsBetween(self, start, end): ...
    def rangeBetween(self, start, end): ...
