import logging

from referencelistparser.states.base import BaseState
from scriptureref import ScriptureRef

logger = logging.getLogger(__file__)


class ReferenceState(BaseState):
    def __init__(self, old_state, book):
        super().__init__(old_state)
        self.book = book
        self.url = None

    def handle_start_tag(self, tag, attrs):
        if tag == 'a':
            self.url = dict(attrs)['href']
            logger.debug('Reference found, processing')
        else:
            logger.debug('Ignoring tag %s', tag)
        return self

    def handle_data(self, data, references):
        references[self.book].append(ScriptureRef(self.url, data))
