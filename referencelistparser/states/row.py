import logging

from referencelistparser.states.base import BaseState
from referencelistparser.states.tabledata import TableDataState

logger = logging.getLogger(__file__)


class RowState(BaseState):
    def handle_start_tag(self, tag, attrs):
        if tag == 'tr':
            logger.debug('Row found, looking for data')
            return TableDataState(self)
        logger.debug('Ignoring tag %s', tag)
        return self

    def handle_end_tag(self, tag):
        if tag == 'tbody':
            return self.old_state
        return self
