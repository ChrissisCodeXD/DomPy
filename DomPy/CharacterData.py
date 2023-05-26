from __future__ import annotations
import DomPy
from abc import ABC, abstractmethod
from typing import Optional, List, Any


class CharacterData(DomPy.Node, ABC):
    def __init__(self, data: str, node_type: DomPy.NodeType):
        super().__init__(node_type)
        self._data = data

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str):
        self._data = value

    @property
    def textContent(self) -> str:
        return self.data

    @property
    def nodeName(self) -> str:
        return '#character-data'

    def contains(self, other: 'Node') -> bool:
        return False


class Text(CharacterData):
    def __init__(self, data: str):
        super().__init__(data, DomPy.NodeType.TEXT_NODE)

    @property
    def nodeName(self) -> str:
        return '#text'


class Comment(CharacterData):
    def __init__(self, data: str):
        super().__init__(data, DomPy.NodeType.COMMENT_NODE)

    @property
    def nodeName(self) -> str:
        return '#comment'
