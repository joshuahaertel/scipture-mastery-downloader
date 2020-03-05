import logging

from referencelistparser.states.base import BaseState
from referencelistparser.states.paragraph import ParagraphState

logger = logging.getLogger(__file__)


class TableDataState(BaseState):
    COLUMN_TO_BOOK_DICT = {
        1: 'OldTestament',
        2: 'NewTestament',
        3: 'BookOfMormon',
        4: 'DoctrineAndCovenants',
    }

    def __init__(self, old_state):
        super().__init__(old_state)
        self.column = 0

    def handle_start_tag(self, tag, attrs):
        if tag == 'td':
            self.column += 1
            book = self.COLUMN_TO_BOOK_DICT[self.column]
            logger.debug('Data found, book: %s. Looking for paragraph', book)
            return ParagraphState(self, book)
        logger.debug('Ignoring tag %s', tag)
        return self

    def handle_end_tag(self, tag):
        if self.column < 4:
            logger.debug('Looking for next column')
            return self
        logger.debug('Tag(%s): Going to next row', tag)
        return self.old_state
