import typing
from typing import Optional, MutableSequence, MutableMapping

__all__ = ("Sanitizer", "SanitizerSettings")


def bold_span_to_strong(element):
    if element.tag == "span" and "bold" in element.get("style", ""):
        element.tag = "strong"
    return element


def italic_span_to_em(element):
    if element.tag == "span" and "italic" in element.get("style", ""):
        element.tag = "em"
    return element


def tag_replacer(from_, to_):
    def replacer(element):
        if element.tag == from_:
            element.tag = to_
        return element

    return replacer


def target_blank_noopener(element):
    if (
            element.tag == "a"
            and element.attrib.get("target") == "_blank"
            and "noopener" not in element.attrib.get("rel", "")
    ):
        element.attrib["rel"] = " ".join(
            part for part in (element.attrib.get("rel", ""), "noopener") if part
        )
    return element


def anchor_id_to_name(element):
    if (
            element.tag == "a"
            and element.attrib.get("id")
            and not element.attrib.get("name")
    ):
        element.attrib["name"] = element.attrib["id"]
    return element


def sanitize_href(href):
    """
    Verify that a given href is benign and allowed.

    This is a stupid check, which probably should be much more elaborate
    to be safe.
    """
    if href.startswith(("/", "mailto:", "http:", "https:", "#", "tel:")):
        return href
    return "#"


DEFAULT_SETTINGS = {
    "allowElements": None,
    "blockElements": None,
    "dropElements": None,
    "allowAttributes": None,
    "dropAttributes": None,
    "allowCustomElements": False,
    "allowComments": False,
}


class SanitizerSettings:

    def __init__(self, **kwargs):
        self.allowElements: Optional[MutableSequence[str]] = kwargs.get("allowElements", DEFAULT_SETTINGS["allowElements"])
        self.blockElements: Optional[MutableSequence[str]] = kwargs.get("blockElements", DEFAULT_SETTINGS["blockElements"])
        self.dropElements: Optional[MutableSequence[str]] = kwargs.get("dropElements", DEFAULT_SETTINGS["dropElements"])
        self.allowAttributes: Optional[MutableMapping[str, Optional[MutableSequence[str]]]] = kwargs.get("allowAttributes", DEFAULT_SETTINGS["allowAttributes"])
        self.dropAttributes: Optional[MutableMapping[str, Optional[MutableSequence[str]]]] = kwargs.get("dropAttributes", DEFAULT_SETTINGS["dropAttributes"])
        self.allowCustomElements: bool = kwargs.get("allowCustomElements", DEFAULT_SETTINGS["allowCustomElements"])
        self.allowComments: bool = kwargs.get("allowComments", DEFAULT_SETTINGS["allowComments"])



class Sanitizer:

    def __init__(self, options: SanitizerSettings = SanitizerSettings()):
        self.options: SanitizerSettings = options
