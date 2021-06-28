import json
from typing import Union, Dict
from dataclasses import dataclass, asdict, fields


class SerializationError(Exception):
    pass


@dataclass
class Base:
    """
    Base Object for all game state dataclasses
    """

    def to_json(self):
        """
        Convert object to JSON

        :return: JSON string
        """
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, data: Union[str, Dict]):
        """
        Converts JSON string or dict to object

        :param data: JSON string or dict
        :return: new instance of class
        :raises SerializationError when data has unknown attributes
        """

        # load JSON if string
        if isinstance(data, str):
            new_data = json.loads(data)

        # just use dict if it is already a dict
        elif isinstance(data, dict):
            new_data = data

        # If somehow unsupported type, use empty dict
        else:
            new_data = {}

        # Dataclasses do not support keyword arguments so we have to convert
        # them into positional through a list and a check that they exist
        args = []

        for k in fields(cls):
            if k.name not in new_data:
                raise SerializationError("Missing attribute: " + k.name)

            # Call recursively the serialization of a sub object, if necessary
            if issubclass(Base, k.type):
                v = k.type.from_json(new_data[k.name])
            else:
                v = new_data[k.name]

            args.append(v)

        return cls(*args)

