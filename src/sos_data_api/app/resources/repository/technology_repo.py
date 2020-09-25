"""
TODO
    update
    add_tags_by_name
"""

from typing import Iterable, List

from ..collections.technology_data import TechnologyData
from ...models.entity.technology_entity import TechnologyEntity
from ...models.repository.technology_base import TechnologyBase


class TechnologyRepo(TechnologyBase):

    def persist(self, tech: TechnologyEntity) -> None:
        """docstring"""
        TechnologyData(name=tech.name, tags=tech.tags).save()

    def find_by_name(self, name: str) -> dict:
        """docstring"""
        return TechnologyData.objects(name=name).first()

    def find_by_uid(self, u_id: str) -> None:
        """docstring"""
        return TechnologyData.objects(id=u_id)

    def find_all(self) -> List[dict]:
        return TechnologyData.objects()

    def update(self, tech: TechnologyEntity) -> None:
        """TODO"""
        doc = self.find_by_uid(tech.u_id)
        doc = None

    def add_tags_by_name(self, name: str, new_tags: Iterable[str]) -> None:
        """docstring"""
        data = self.find_by_name(name)
        tech = Technology(
            u_id=data["_id"], name=data["name"], tags=data["tags"])

        tech.tags += new_tags
        # check if id does upsert!
        self.perssit(tech)

    def delete(self, tech: TechnologyEntity) -> None:
        """TODO"""
        doc = self.find_by_uid(tech.u_id)
        doc.delete()
