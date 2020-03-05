import logging

logger = logging.getLogger(__file__)


class BaseState:
    def __init__(self, old_state):
        self.old_state = old_state

    def handle_start_tag(self, tag, attrs):
        raise NotImplementedError

    def handle_data(self, data, references):
        raise ValueError(
            f'{type(self).__name__}: Tag should not have data({data})'
        )

    def handle_end_tag(self, tag):
        logger.debug(
            f'Tag(%s): Going from %s to %s', tag, type(self).__name__,
            type(self.old_state).__name__
        )
        return self.old_state
