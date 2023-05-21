import typing


class Document:

    def __init__(self):
        self._className: typing.Optional[str] = None



    @property
    def className(self) -> typing.Optional[str]:
        return self._className

    @className.setter
    def className(self, value: typing.Any) -> None:
        self._className = str(value) if value is not None else None
