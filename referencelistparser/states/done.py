import logging

from referencelistparser.states.base import BaseState

logger = logging.getLogger(__file__)


class DoneState(BaseState):
    def handle_start_tag(self, tag, attrs):
        return self

    def handle_end_tag(self, tag):
        return self

    def handle_data(self, data, references):
        return None
