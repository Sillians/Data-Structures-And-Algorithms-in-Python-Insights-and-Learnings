### Python’s Enum Definition:
Source: https://docs.python.org/3/library/enum.html
- https://docs.python.org/3/howto/enum.html#enum-basic-tutorial
- https://docs.python.org/3/howto/enum.html#enum-advanced-tutorial
- https://docs.python.org/3/howto/enum.html#enum-cookbook

An enumeration:
- is a set of symbolic names (members) bound to unique values.
- can be iterated over to return its canonical (i.e. non-alias) members in definition order.
- uses call syntax to return members by value.
- uses index syntax to return members by name.

N/B: Member values can be anything: `int`, `str`, etc. If the exact value is unimportant you may use auto 
instances and an appropriate value will be chosen for you. 

While mutable/unhashable values, such as `dict`, `list` or a mutable dataclass, can be used, 
they will have a quadratic performance impact during creation relative to the total number of 
mutable/unhashable values in the enum.

### Module Contents
- EnumType: The type for Enum and its subclasses.
- Enum: Base class for creating enumerated constants.
- IntEnum: Base class for creating enumerated constants that are also subclasses of `int`.
- StrEnum: Base class for creating enumerated constants that are also subclasses of str.
- ReprEnum: Used by IntEnum, StrEnum, and IntFlag to keep the `str()` of the mixed-in type.
- property(): Allows Enum members to have attributes without conflicting with member names. The `value` and `name` attributes are implemented this way.
- etc.

