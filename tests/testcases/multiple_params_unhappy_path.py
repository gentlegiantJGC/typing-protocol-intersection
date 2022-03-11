from types import SimpleNamespace
from typing import Dict, Generic, Protocol, TypeVar

from typing_protocol_intersection import ProtocolIntersection


class HasX(Protocol):
    x: str


class HasY(Protocol):
    y: str


class HasZ(Protocol):
    z: str


T = TypeVar("T")


class Builder(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self._d: Dict[str, str] = {}

    def with_x(self) -> "Builder[ProtocolIntersection[T, HasX]]":
        self._d["x"] = "X"
        return self  # type: ignore

    def with_y(self) -> "Builder[ProtocolIntersection[T, HasY]]":
        self._d["y"] = "Y"
        return self  # type: ignore

    def with_z(self) -> "Builder[ProtocolIntersection[T, HasZ]]":
        self._d["z"] = "Z"
        return self  # type: ignore

    def build(self) -> T:
        return SimpleNamespace(**self._d)  # type: ignore


def get_x_y_z(o: ProtocolIntersection[HasX, HasY, HasZ]) -> None:
    print(f"{o.x=}; {o.y=}; {o.z=}")


def main() -> None:
    valid_o = Builder().with_x().with_y().build()
    get_x_y_z(valid_o)


# expected stdout
# tests/testcases/multiple_params_unhappy_path.py:49:15: error: Argument 1 to "get_x_y_z" has incompatible type "typing_protocol_intersection.types.ProtocolIntersection[HasY, HasX]"; expected "typing_protocol_intersection.types.ProtocolIntersection[HasZ, HasY, HasX]"  [arg-type]
# tests/testcases/multiple_params_unhappy_path.py:49:15: note: "ProtocolIntersection" is missing following "ProtocolIntersection" protocol member:
# tests/testcases/multiple_params_unhappy_path.py:49:15: note:     z
# Found 1 error in 1 file (checked 1 source file)
