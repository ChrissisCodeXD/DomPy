from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List, Any

from DomPy.Errors import NotFoundError


class NodeType(Enum):
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11


class NodeList:
    def __init__(self):
        self._nodes = []

    def __len__(self):
        return len(self._nodes)

    def __getitem__(self, index):
        return self._nodes[index]

    def append(self, node):
        self._nodes.append(node)

    def remove(self, node):
        self._nodes.remove(node)

    def values(self):
        return self._nodes

    def keys(self):
        return range(len(self._nodes))

    def entries(self):
        return zip(self.keys(), self.values())

    def forEach(self, callback):
        for node in self._nodes:
            callback(node)

    def item(self, index):
        try:
            return self._nodes[index]
        except IndexError:
            return None

    def insert(self, index, node):
        self._nodes.insert(index, node)

    def clear(self):
        self._nodes.clear()

    def __contains__(self, item):
        return item in self._nodes


class Node(ABC):

    def __init__(self, node_type: NodeType, owner_document: Optional['Document'] = None):
        self._node_type: NodeType = node_type
        self._childNodes: NodeList = NodeList()
        self._nodeValue: Optional[Any] = None
        self._parentNode: Optional[Node] = None
        self._isConnected: bool = False
        self._baseURI: Optional[str] = None
        self._ownerDocument: Optional['Document'] = owner_document

    @property
    def nodeType(self) -> NodeType:
        return self._node_type

    @property
    def baseURI(self) -> Optional[str]:
        return self._baseURI

    @baseURI.setter
    def baseURI(self, value: Any):
        self._baseURI = str(value)

    @property
    def childNodes(self) -> NodeList:
        return self._childNodes

    @property
    def firstChild(self) -> Optional['Node']:
        return self._childNodes[0] if self._childNodes else None

    @property
    def isConnected(self) -> bool:
        return self._isConnected

    @property
    def lastChild(self) -> Optional['Node']:
        return self._childNodes[-1] if self._childNodes else None

    @property
    @abstractmethod
    def nodeName(self) -> str:
        pass

    @property
    def nodeValue(self) -> str:
        return self._nodeValue

    @property
    def ownerDocument(self) -> 'Document':
        return self._ownerDocument

    @property
    def parentNode(self) -> Optional['Node']:
        return self._parentNode

    @property
    def textContent(self):
        return ''.join(child.textContent for child in self.childNodes if
                       child.nodeType in [NodeType.TEXT_NODE, NodeType.ELEMENT_NODE])

    @textContent.setter
    def textContent(self, text):
        while self.firstChild:
            self.removeChild(self.firstChild)

        # ToDo
        # self.appendChild(TextNode(text))

    @abstractmethod
    def appendChild(self, child: 'Node') -> 'Node':
        pass

    @abstractmethod
    def cloneNode(self, deep: bool = False) -> 'Node':
        pass

    @abstractmethod
    def compareDocumentPosition(self, other: 'Node') -> int:
        pass

    @abstractmethod
    def contains(self, other: 'Node') -> bool:
        pass

    @abstractmethod
    def getRootNode(self) -> 'Node':
        pass

    @abstractmethod
    def hasChildNodes(self) -> bool:
        pass

    def insertBefore(self, newNode: 'Node', referenceNode: 'Node') -> 'Node':
        for index, child in self.childNodes.entries():
            if child == referenceNode:
                self.childNodes.insert(index, newNode)
                return newNode

    @abstractmethod
    def isDefaultNamespace(self, namespaceURI: str) -> bool:
        pass

    @abstractmethod
    def isEqualNode(self, other: 'Node') -> bool:
        pass

    @abstractmethod
    def isSameNode(self, other: 'Node') -> bool:
        pass

    @abstractmethod
    def lookupPrefix(self, namespaceURI: str) -> Optional[str]:
        pass

    @abstractmethod
    def lookupNamespaceURI(self, prefix: Optional[str]) -> Optional[str]:
        pass

    @abstractmethod
    def normalize(self) -> None:
        pass

    def removeChild(self, child: 'Node') -> 'Node':
        if child in self.childNodes:
            self.childNodes.remove(child)
            return child
        raise NotFoundError(f'Node {child} not found in {self}')

    def replaceChild(self, newChild: 'Node', oldChild: 'Node') -> 'Node':
        for index, child in self.childNodes.entries():
            if child == oldChild:
                self.childNodes[index] = newChild
                return oldChild
        raise NotFoundError(f'Node {oldChild} not found in {self}')
