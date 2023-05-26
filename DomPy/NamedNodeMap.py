from __future__ import annotations
from typing import Optional
from DomPy.Errors import NotFoundError


class Attr:
    def __init__(self, name: str, value: Optional[str], owner_element: 'Element', namespace: Optional[str] = None):
        self._name: str = name
        self._value: Optional[str] = value
        self._owner_element: 'Element' = owner_element
        self._namespace: Optional[str] = namespace

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, val: str):
        self._value = str(val)

    @property
    def ownerElement(self) -> 'Element':
        return self._owner_element

    @property
    def namespaceURI(self) -> Optional[str]:
        return self._namespace


class NamedNodeMap:

    def __init__(self):
        self._map = {}

    def getNamedItem(self, name: str) -> Optional[Attr]:
        return self._map.get(name)

    def getNamedItemNS(self, namespace: str, local_name: str) -> Optional[Attr]:
        for attr in self._map.values():
            if attr.namespaceURI == namespace and attr.name == local_name:
                return attr
        return None

    def item(self, index: int) -> Optional[Attr]:
        return list(self._map.keys())[index]

    def __getitem__(self, index: int) -> Optional[Attr]:
        return list(self._map.values())[index]

    def removeNamedItem(self, attrName: str) -> Optional[Attr]:
        if attrName in self._map:
            attribute: Attr = self._map[attrName]
            del self._map[attrName]
            return attribute
        else:
            raise NotFoundError(f'Attribute {attrName} not found')

    def removeNamedItemNS(self, namespace: str, local_name: str) -> Optional[Attr]:
        for attr in self._map.values():
            if attr.namespaceURI == namespace and attr.name == local_name:
                del self._map[attr.name]
                return attr
        raise NotFoundError(f'Attribute {local_name} not found in namespace {namespace}')

    def setNamedItem(self, attr: Attr) -> Optional[Attr]:
        if self.hasNamedItem(attr.name):
            old_attr = self._map[attr.name]
            self._map[attr.name] = attr
            return old_attr
        self._map[attr.name] = attr

    def setNamedItemNS(self, attr: Attr) -> Optional[Attr]:
        if self.hasNamedItemNS(attr.namespaceURI, attr.name):
            old_attr = self._map[attr.name]
            self._map[attr.name] = attr
            return old_attr
        self._map[attr.name] = attr

    def hasNamedItem(self, name: str) -> bool:
        return name in self._map

    def hasNamedItemNS(self, namespace: str, local_name: str) -> bool:
        for attr in self._map.values():
            if attr.namespaceURI == namespace and attr.name == local_name:
                return True
        return False

    def __len__(self):
        return len(self._map)
