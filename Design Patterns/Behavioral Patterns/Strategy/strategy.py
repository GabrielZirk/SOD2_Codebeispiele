

# not required but a good idea
from abc import ABC, abstractmethod
from enum import auto, Enum


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class ListStrategy(ABC):
    @abstractmethod
    def formate_list(self, buffer): pass



class MarkdownListStrategy(ListStrategy):
    def formate_list(self, buffer, items):
        for item in items:
            buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def formate_list(self, buffer, items):
        buffer.append('<ul>\n')
        for item in items:
            buffer.append(f'  <li>{item}</li>\n')
        buffer.append('</ul>\n')

class TextProcessor:
    def __init__(self):
        self.buffer = []
        self.list_strategy = None

    def append_list(self, textdatei: str):
        file = open(textdatei, "r")
        lines = file.read().splitlines()
        self.list_strategy.formate_list(self.buffer, lines)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            # print(type(format))
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)

if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']
    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list("text.txt")
    print(tp)
    tp.clear()
