import logging

from referencelistparser.states.base import BaseState
from referencelistparser.states.row import RowState

logger = logging.getLogger(__file__)


class StartState(BaseState):
    def handle_start_tag(self, tag, attrs):
        if tag == 'tbody':
            logger.debug('Table found, looking for rows')
            return RowState(self)
        return self

    def handle_data(self, data, references):
        return None

    def handle_end_tag(self, tag):
        if tag != 'tbody':
            return self
        logger.debug('Ignoring tag %s', tag)
        return super().handle_end_tag(tag)
