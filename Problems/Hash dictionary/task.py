from collections.abc import Hashable

objects_dict = {}
for _object in objects:
    if isinstance(_object, Hashable):
        objects_dict[_object] = _object.__hash__()
