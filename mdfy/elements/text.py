import abc
import re
from typing import Dict, Optional

from lark import Lark, Token, Tree
from lark.visitors import Interpreter

from ._base import MdElement


class MdTextInterpreter(Interpreter):
    """Lark Interpreter tailored for MdText interpreting styled text.

    Args:
        style_patterns (Dict[str, str]): A dictionary mapping style names to formatting strings.
    """

    def __init__(self, style_patterns: Dict[str, str]):
        super().__init__()
        self.style_patterns = style_patterns

    def process_content_tree(self, tree: Tree) -> str:
        """Processes a subtree for content in yled text.

        Args:
            tree (Tree): The subtree to process.

        Returns:
            str: The processed text.
        """
        interpreted = ""
        for child in tree.children:
            if isinstance(child, Token):
                interpreted += child.value
            elif isinstance(child, Tree):
                interpreted += self.styled_text(child)
            else:
                raise ValueError(f"Unable to handle this child type: {child.__class__}")
        return interpreted

    def styled_text(self, tree: Tree) -> str:
        """Processes a subtree for styled text.

        Args:
            tree (Tree): The subtree to process.

        Returns:
            str: The styled text.
        """
        _, *content, _, style, _ = tree.children

        target_text = ""
        for tree in content:
            target_text += self.process_content_tree(tree)

        if not isinstance(style, Token):
            raise ValueError(f"Expected style to be a Token, got {style.__class__}")

        if style.value in self.style_patterns:
            return self.style_patterns[style.value].format(target_text)
        else:
            return target_text

    def start(self, tree: Tree) -> str:
        return "".join(self.visit_children(tree))


grammar = r"""
    start: TEXT? styled_text? (start)* TEXT?
    styled_text: LBRACE content+ COLON INTEXT RBRACE
    content: INTEXT | INTEXT? styled_text
    TEXT:   WS* /[^{}]+/ WS*
    INTEXT: WS* /[^{}:]+/ WS*
    LBRACE: "{"
    RBRACE: "}"
    COLON: ":"

    %import common.WS
"""


class MdFormatter(abc.ABC):
    """Abstract base class for Markdown formatters."""

    @abc.abstractmethod
    def format(self, text: str) -> str:
        """Formats the text and returns the formatted text.

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text.
        """
        raise NotImplementedError


class MdTextFormatter(MdFormatter):
    """Markdown Text Formatter to handle text styling based on a specified grammar and style patterns.

    Attributes:
        grammar (str): The grammar to be used for parsing the text.
        interpreter (Interpreter): The interpreter to be used for interpreting the parsed text.
        patterns (Dict[str, str]): Expanded style patterns including aliases.
    """

    STYLE_PATTERNS = {
        "strong": "***{}***",
        "bold": "**{}**",
        "italic": "*{}*",
        "not": "~~{}~~",
        "underline": "<u>{}</u>",
        "quote": "`{}`",
    }

    STYLE_ALIASES = {
        "strong": ["st"],
        "bold": ["bo", "bd"],
        "italic": ["it"],
        "not": ["no", "nt"],
        "underline": ["un", "ul"],
        "quote": ["qu", "qt"],
    }

    def __init__(
        self,
        grammar: str = grammar,
        interpreter: Optional[Interpreter] = None,
        patterns: Optional[dict] = None,
    ):
        self.grammar = grammar
        if self.grammar is None:
            raise ValueError("Grammar cannot be None")
        self.parser = Lark(self.grammar)

        if patterns is None:
            patterns = self.expand_style_patterns(
                self.STYLE_PATTERNS, self.STYLE_ALIASES
            )
        self.patterns = patterns

        if interpreter is None:
            interpreter = MdTextInterpreter(self.patterns)
        self.interpreter = interpreter

    def expand_style_patterns(self, base_patterns: dict, aliases: dict) -> dict:
        """Expands the style patterns with aliases.

        Args:
            base_patterns (Dict[str, str]): Base style patterns.
            aliases (Dict[str, str]): Aliases for the style names.

        Returns:
            Dict[str, str]: Expanded style patterns.
        """
        expand_patterns = {
            alias: base_patterns[style_name]
            for style_name, aliases in aliases.items()
            for alias in aliases
        }
        return {**base_patterns, **expand_patterns}

    def format(self, text: str) -> str:
        """Formats the text for style markers and returns the formatted text.

        Args:
            text (str): The text to be formatted.

        Returns:
            str: The formatted text.
        """
        parsed = self.parse(text)
        result: str = self.interpreter.visit(parsed)
        return result

    def parse(self, text: str) -> Tree:
        """Parses the text for style markers and returns the parsed text.

        Args:
            text (str): The text to be parsed.

        Returns:
            lark.Tree: The parsed syntax tree.
        """
        return self.parser.parse(text)


class MdText(MdElement):
    """MdElementt class to handle the text and styling of text.

    Attributes:
        content (str): The content string containing potential style markers.
        formatter (MdFormatter): The formatter to apply styling to the content.

    Examples:
        >>> text = MdText("This is {bold:bold} text.")
        >>> print(text)
        This is **bold** text.
        >>> MdText("{This is underline text:underline}.").to_str()
        <u>This is underline text</u>.
        >>> MdText("{This is {nested:bold} style text:underline}.").to_str()
        <u>This is **nested** style text</u>.
        >>> MdText("You can use aliases e.g. {st:st}  {bd:bo}.").to_str()
        You can use aliases e.g. ***st***  **bd**.

    Note:
        Available style patterns:
            - strong: bold text (e.g. `***strong***`)
            - bold: bold text (e.g. `**bold**`)
            - italic: italic text (e.g. {*italic*})
            - not: strike-through text (e.g. `~~strike-through~~`)
            - underline: underlined text (e.g. `<u>underlined</u>`)
            - quote: quoted text (e.g. `\`quoted\``)

        Also, the following aliases are available for the style patterns:
            - strong: st
            - bold: bo, bd
            - italic: it
            - not: no, nt
            - underline: un, ul
            - quote: qu, qt
    """

    def __init__(self, content: str, formatter: MdFormatter = MdTextFormatter()):
        """Initializes an instance of the MdText class to handle the text and styling of text.

        Args:
            content (str): The content string containing potential style markers.
            formatter (MdFormatter, optional): The formatter to apply styling to the content.
                                                     Defaults to MdTextFormatter().
        """

        self.content = content
        self.formatter = formatter

    def __str__(self) -> str:
        """Returns the styled content as per the specified style markers.

        Returns:
            str: Formatted markdown string with the appropriate styles applied.
        """
        result = self.content
        result = self.formatter.format(result)

        return result

    def __add__(self, other: "MdText") -> "MdText":
        """Adds two MdText objects together.

        Args:
            other (MdText): The other MdText object to be added.

        Returns:
            MdText: A new MdText object containing the concatenated content of the two objects.
        """
        return MdText(str(self) + str(other))
