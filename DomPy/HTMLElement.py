import DomPy
from DomPy import Element
from typing import Optional, Union
from enum import Enum


class contentEditable(Enum):
    TRUE = "true"
    FALSE = "false"
    INHERIT = "inherit"



class HTMLElement(Element):

    def __init__(self, tag_name):
        super().__init__(tag_name)
        self._accessKey: Optional[str] = None
        self._editable: contentEditable = contentEditable.INHERIT
        self._dataset: DomPy.DOMStringMap = DomPy.DOMStringMap()

    @property
    def accessKey(self) -> str:
        return self._accessKey

    @accessKey.setter
    def accessKey(self, val: str):
        self._accessKey = str(val)

    @property
    def accessKeyLabel(self) -> str:
        raise NotImplementedError("accessKeyLabel is not implemented")

    @property
    def contentEditable(self) -> str:
        return self._editable.value

    @contentEditable.setter
    def contentEditable(self, val: Union[str, contentEditable]):
        if isinstance(val, str):
            self._editable = contentEditable(val)
        elif isinstance(val, contentEditable):
            self._editable = val
        else:
            raise TypeError("contentEditable must be str or contentEditable")

    @property
    def dataset(self) -> DomPy.DOMStringMap:
        return self._dataset

    @dataset.setter
    def dataset(self, val: DomPy.DOMStringMap):
        if isinstance(val, DomPy.DOMStringMap):
            self._dataset = val
        else:
            raise TypeError("dataset must be DOMStringMap")

    @property
    def dir(self) -> str:
        raise NotImplementedError("dir is not implemented") #TODO




