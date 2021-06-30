from steam_gsi.games import Base
from dataclasses import dataclass, field


def test_base_from_json():

    @dataclass
    class Thing(Base):
        a: str = field()
        b: str = field()

    json_string = '{"a": "a", "b": "b"}'
    t = Thing.from_json(json_string)

    assert t.a == "a"
    assert t.b == "b"


def test_base_to_json():

    @dataclass
    class Thing(Base):
        a: str = field()
        b: str = field()

    t = Thing("a", "b")

    assert t.to_json() == '{"a": "a", "b": "b"}'


def test_base_json():
    @dataclass
    class Thing(Base):
        a: str = field()
        b: str = field()

    json_string = '{"a": "a", "b": "b"}'

    t = Thing.from_json(json_string)
    t2 = Thing.from_json(t.to_json())

    assert t.a == t2.a
    assert t.b == t2.b

