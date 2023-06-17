from abc import ABC, abstractmethod


class IHittingTarget(ABC):
    @abstractmethod
    def _hit_target(self, target_type: str, quantity: int): ...
