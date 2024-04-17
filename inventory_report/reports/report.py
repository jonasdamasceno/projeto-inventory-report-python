from typing import Protocol


class Report(Protocol):
    def add_inventory(self, inventory) -> None:
        pass

    def generate(self) -> str:
        pass
