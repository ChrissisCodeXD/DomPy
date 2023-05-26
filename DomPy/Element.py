from __future__ import annotations
from typing import Optional, Union
import DomPy
from DomPy.Errors import NotFoundError


class Element(DomPy.Node):

    def __init__(self, tag_name: str):
        super().__init__(DomPy.NodeType.ELEMENT_NODE)
        self._tagName = tag_name
        self._attributes = DomPy.NamedNodeMap()

    @property
    def tagName(self) -> str:
        return self._tagName

    @property
    def nodeName(self) -> str:
        return self.tagName

    def appendChild(self, child: 'Node') -> 'Node':
        self._childNodes.append(child)

    def cloneNode(self, deep: bool = False) -> 'Node':
        pass #TODO

    def compareDocumentPosition(self, other: 'Node') -> int:
        pass #TODO

    def contains(self, other: 'Node') -> bool:
        if self._childNodes.values().__contains__(other):
            return True
        else:
            for child in self._childNodes:
                if child.contains(other):
                    return True
        return False

    def getRootNode(self) -> 'Node':
        t_node: 'Node' = self
        while t_node.parentNode is not None:
            t_node = t_node.parentNode
        return t_node

    def hasChildNodes(self) -> bool:
        return bool(self._childNodes)

    def isDefaultNamespace(self, namespaceURI: str) -> bool:
        pass #TODO

    def isEqualNode(self, other: 'Node') -> bool:
        pass #TODO

    def isSameNode(self, other: 'Node') -> bool:
        return self is other

    def lookupPrefix(self, namespaceURI: str) -> Optional[str]:
        pass #TODO

    def lookupNamespaceURI(self, prefix: Optional[str]) -> Optional[str]:
        pass #TODO

    def normalize(self) -> None:
        pass #TODO

    def getAttribute(self, name: str) -> Optional[str]:
        attr = self._attributes.getNamedItem(name)
        if attr is None:
            return None
        else:
            return attr.value

    def getAttributeNames(self) -> list[str]:
        return [attr.name for attr in self._attributes]

    def getAttributeNode(self, attr_name: str) -> Optional[DomPy.Attr]:
        return self._attributes.getNamedItem(attr_name)

    def getAttributeNodeNS(self, namespace: str, local_name: str) -> Optional[DomPy.Attr]:
        return self._attributes.getNamedItemNS(namespace, local_name)

    def getAttributeNS(self, namespace: str, local_name: str) -> Optional[str]:
        attr = self._attributes.getNamedItemNS(namespace, local_name)
        if attr is None:
            return None
        else:
            return attr.value

    def getElementsByClassName(self, class_name: str) -> list[DomPy.Element]:
        pass #TODO

    def getElementsByTagName(self, tag_name: str) -> list[DomPy.Element]:
        pass #TODO

    def getElementsByTagNameNS(self, namespace: str, local_name: str) -> list[DomPy.Element]:
        pass #TODO

    def hasAttribute(self, name: str) -> bool:
        return self._attributes.getNamedItem(name) is not None

    def hasAttributeNS(self, namespace: str, local_name: str) -> bool:
        return self._attributes.getNamedItemNS(namespace, local_name) is not None

    def hasAttributes(self) -> bool:
        return len(self._attributes) > 0

    def insertAdjacentElement(self, position: str, element: DomPy.Element) -> Optional[DomPy.Element]:
        pass #TODO

    def insertAdjacentHTML(self, position: str, text: str) -> None:
        pass #TODO

    def insertAdjacentText(self, position: str, text: str) -> None:
        pass #TODO

    def matches(self, selector: str) -> bool:
        pass #TODO

    def prepend(self, *nodes: Union[DomPy.Node, str]) -> None:
        pass #TODO

    def querySelector(self, selector: str) -> Optional[DomPy.Element]:
        pass #TODO

    def querySelectorAll(self, selector: str) -> DomPy.NodeList:
        pass #TODO

    def remove(self) -> None:
        pass #TODO

    def removeAttribute(self, name: str) -> None:
        self._attributes.removeNamedItem(name)

    def removeAttributeNode(self, attr: DomPy.Attr) -> DomPy.Attr:
        return self._attributes.removeNamedItem(attr.name)

    def removeAttributeNS(self, namespace: str, local_name: str) -> None:
        self._attributes.removeNamedItemNS(namespace, local_name)

    def replaceChildren(self, *nodes: Union[DomPy.Node, str]) -> None:
        self._childNodes.clear()
        for node in nodes:
            if isinstance(node, DomPy.Node):
                self._childNodes.append(node)
            elif isinstance(node, str):
                self._childNodes.append(DomPy.Text(node))

    def replaceWith(self, *nodes: Union[DomPy.Node, str]) -> None:
        for node in nodes:
            if isinstance(node, DomPy.Node):
                self._parentNode.insertBefore(node, self)
            elif isinstance(node, str):
                self._parentNode.insertBefore(DomPy.Text(node), self)
        self._parentNode.removeChild(self)

    def setAttribute(self, name: str, value: Optional[str]) -> None:
        self._attributes.setNamedItem(DomPy.Attr(name, value, self))

    def setAttributeNode(self, attr: DomPy.Attr) -> Optional[DomPy.Attr]:
        return self._attributes.setNamedItem(attr)

    def setAttributeNodeNS(self, attr: DomPy.Attr) -> Optional[DomPy.Attr]:
        return self._attributes.setNamedItemNS(attr)

    def setAttributeNS(self, namespace: str, name: str, value: str) -> None:
        self._attributes.setNamedItemNS(DomPy.Attr(name, value, self, namespace))

    def setHTML(self, input: str, sanitizer: Optional['Sanitizer'] = None) -> None:
        pass #TODO

    def toggleAttribute(self, name: str, force: Optional[bool] = None) -> bool:
        if force is None:
            if self.hasAttribute(name):
                self.removeAttribute(name)
                return False
            else:
                self.setAttribute(name, None)
                return True
        elif force:
            self.setAttribute(name, None)
            return True
        else:
            try:
                self.removeAttribute(name)
            except NotFoundError:
                pass
            return False



