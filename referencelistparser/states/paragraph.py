import logging

from referencelistparser.states.base import BaseState
from referencelistparser.states.reference import ReferenceState

logger = logging.getLogger(__file__)


class ParagraphState(BaseState):
    def __init__(self, old_state, book):
        super().__init__(old_state)
        self.book = book

    def handle_start_tag(self, tag, attrs):
        if tag == 'p':
            logger.debug('Paragraph found, looking for reference')
            return ReferenceState(self, self.book)
        logger.debug('Ignoring tag %s', tag)
        return self
