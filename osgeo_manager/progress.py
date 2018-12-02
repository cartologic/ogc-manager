from abc import ABCMeta, abstractmethod

from .log import get_logger


class BaseProgress(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.logger = get_logger(__name__)

    @abstractmethod
    def on_start(self, *args, **kwargs):
        pass

    @abstractmethod
    def on_step(self, *args, **kwargs):
        pass

    @abstractmethod
    def on_finish(self, *args, **kwargs):
        pass

    @abstractmethod
    def on_error(self, *args, **kwargs):
        pass
