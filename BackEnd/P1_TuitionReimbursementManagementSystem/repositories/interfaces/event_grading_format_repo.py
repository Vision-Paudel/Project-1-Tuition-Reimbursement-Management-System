from abc import ABC, abstractmethod


class EventGradingFormatRepo(ABC):

    @abstractmethod
    def create_event_grading_format(self, event_grading_format):
        pass

    @abstractmethod
    def get_event_grading_format(self, event_grading_format_id):
        pass

    @abstractmethod
    def get_all_event_grading_formats(self):
        pass

    @abstractmethod
    def update_event_grading_format(self, event_grading_format):
        pass

    @abstractmethod
    def delete_event_grading_format(self, event_grading_format_id):
        pass
