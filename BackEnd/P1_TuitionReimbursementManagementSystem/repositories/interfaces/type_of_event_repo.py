from abc import ABC, abstractmethod


class TypeOfEventRepo(ABC):

    @abstractmethod
    def create_type_of_event(self, type_of_event):
        pass

    @abstractmethod
    def get_type_of_event(self, event_id):
        pass

    @abstractmethod
    def get_all_type_of_events(self):
        pass

    @abstractmethod
    def update_type_of_event(self, change):
        pass

    @abstractmethod
    def delete_type_of_event(self, event_id):
        pass
