from typing import List, Iterable

from chia.types.blockchain_format.sized_bytes import bytes32


class IntegrityError(Exception):
    pass


def build_message_with_hashes(message: str, bytes_objects: Iterable[bytes]) -> str:
    return "\n".join([message, *[f"    {b.hex()}" for b in bytes_objects]])


class TreeGenerationIncrementingError(IntegrityError):
    def __init__(self, tree_ids: List[bytes32]) -> None:
        super().__init__(
            build_message_with_hashes(
                message="Found trees with generations not properly incrementing:",
                bytes_objects=tree_ids,
            )
        )
