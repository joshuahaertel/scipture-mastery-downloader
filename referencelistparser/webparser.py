from html.parser import HTMLParser

from referencelistparser.states.base import BaseState
from referencelistparser.states.done import DoneState
from referencelistparser.states.start import StartState


class ScriptureListParser(HTMLParser):
    def error(self, message):
        raise ValueError('AH!')

    def __init__(self, book_references):
        super().__init__()
        self.book_references = book_references
        self.state: BaseState = StartState(DoneState(None))

    def handle_starttag(self, tag, attrs):
        self.state = self.state.handle_start_tag(tag, attrs)

    def handle_data(self, data):
        self.state.handle_data(data, self.book_references)

    def handle_endtag(self, tag):
        self.state = self.state.handle_end_tag(tag)
