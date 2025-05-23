from typing import Dict, Optional
from collections.abc import Callable
import logging

from mdfy.elements.text_formatter import MdFormatter

try:
    import lark
    from lark import Lark, Token, Tree
    from lark.visitors import Interpreter
except ImportError as e:
    raise ImportError(
        "Please install the lark package via `pip install mdfy[styled-text]`"
    ) from e


logger = logging.getLogger(__name__)


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

        children = tree.children
        if len(children) == 1 and isinstance(children[0], Token):
            return str(children[0].value)
        if len(children) == 0:
            return ""

        interpreted = ""
        for child in children:
            if isinstance(child, Token):
                interpreted += child.value
            elif isinstance(child, Tree):
                if child.data == "styled_text":
                    interpreted += self.styled_text(child)
                elif child.data == "non_styled_text":
                    interpreted += self.non_styled_text(child)
                else:
                    raise ValueError(
                        f"Unable to handle this content type: {child.__class__}"
                    )
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
            logger.warning(
                "Style '%s' not found in patterns. Returning unformatted text.",
                style.value,
            )
            return target_text

    def non_styled_text(self, tree: Tree) -> str:
        """Processes a subtree for non-styled text.

        Args:
            tree (Tree): The subtree to process.

        Returns:
            str: The non-styled text.
        """
        lbrak, *content, rbrak = tree.children
        if not isinstance(lbrak, Token) or not isinstance(rbrak, Token):
            raise ValueError(
                f"Expected lbrak and rbrak to be Tokens, got {lbrak.__class__} and {rbrak.__class__}"
            )

        target_texts: list[str] = []
        for node in content:
            target_texts.append(self.process_content_tree(node))

        return str(lbrak.value) + "".join(target_texts) + str(rbrak.value)

    def start(self, tree: Tree) -> str:
        return "".join(self.visit_children(tree))


grammar = r"""
    start: TEXT? non_styled_text? styled_text? (start)* TEXT?
    non_styled_text: LBRAK content+ RBRAK
    styled_text: LBRAK content+ COLON INTEXT RBRAK
    content: INTEXT | INTEXT? non_styled_text? styled_text?
    TEXT:   WS* /[^\[\]]+/ WS*
    INTEXT: WS* /[^\[\]:]+/ WS*
    LBRAK: "["
    RBRAK: "]"
    COLON: ":"

    %import common.WS
"""


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
        "code": "`{}`",
    }

    STYLE_ALIASES = {
        "strong": ["st"],
        "bold": ["bo", "bd"],
        "italic": ["it"],
        "not": ["no", "nt"],
        "underline": ["un", "ul"],
        "code": ["cd", "quote"],
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
        try:
            parsed = self.parse(text)
            result: str = self.interpreter.visit(parsed)
        except lark.exceptions.UnexpectedInput as e:
            logger.warning("Invalid Input: %s. Returning the original text.", e)
            return text

        return result

    def parse(self, text: str) -> Tree:
        """Parses the text for style markers and returns the parsed text.

        Args:
            text (str): The text to be parsed.

        Returns:
            lark.Tree: The parsed syntax tree.
        """
        return self.parser.parse(text)
