


class DOMParser:

    MIME_TYPES = (
        "text/html",
        "text/xml",
        "application/xml",
        "application/xhtml+xml",
        "image/svg+xml"
    )
    def __init__(self):
        pass

    def parseFromString(self, string: str, mimeType: str) -> 'Document':
        if mimeType not in self.MIME_TYPES:
            raise TypeError(f"MIME type `{mimeType}` not supported")
