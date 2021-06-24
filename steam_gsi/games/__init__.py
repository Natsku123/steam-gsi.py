import json
from dataclasses import dataclass, asdict


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
    def from_json(cls, data: str):
        """
        Converts JSON string to object

        :param data: JSON string
        :return: new instance of class
        :raises TypeError when data has more unknown attributes
        """
        return cls(**json.loads(data))

