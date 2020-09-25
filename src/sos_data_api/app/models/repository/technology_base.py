from abc import ABC, abstractmethod
from typing import NoReturn, List

from ..entity.technology_entity import TechnologyEntity


class TechnologyBase(ABC):

    @abstractmethod
    def persist(self, tech: TechnologyEntity) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_by_name(self, name: str) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_by_uid(self, u_id: str) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def update(self, tech: TechnologyEntity) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def add_tags_by_name(self, tech: TechnologyEntity, new_tags: List[str]) -> NoReturn:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, tech: TechnologyEntity) -> NoReturn:
        raise NotImplementedError()
