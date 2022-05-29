from abc import ABC, abstractmethod


class PBInfoBase(ABC):
    def __init__(self, text):
        self.text = text
        self.current_time = self.get_current_time()
        self.pb = self.get_pb()
        self.last_delta = self.get_last_delta()
        self.is_pb_pace = self._get_is_pb_pace()
        self.fraction_of_run = self._get_fraction_of_run()

    @abstractmethod
    def get_current_time(self) -> float:
        """
        returns the current time of the run in seconds (fractions allowed)
        """
        pass

    @abstractmethod
    def get_pb(self) -> float:
        """
        returns the current pb in seconds (fractions allowed)
        """
        pass

    @abstractmethod
    def get_last_delta(self) -> float:
        """
        returns the most recent split delta in seconds, fractions allowed
        """
        pass

    def _get_fraction_of_run(self) -> float:
        if self.pb <= 0:
            return 0
        return (self.pb - self.current_time) / self.pb

    def _get_is_pb_pace(self):
        try:
            return True if self.last_delta < 0 else False
        except TypeError:
            return None
