import typing as t

Messages = t.List[t.Dict[str, str]]
Headers = t.Union[t.Dict[str, str], t.Any]
User_Agent = t.NewType("User_Agent", str)
Any = t.Any
Dict = t.Dict
List = t.List


__all__ = ["Messages", "Headers", "Any", "Dict", "List", "User_Agent"] 

# Path: assets/src/typing.py