from repositories.interfaces.type_of_event_repo import TypeOfEventRepo


class TypeOfEventService:

    def __init__(self, type_of_event_repo: TypeOfEventRepo):
        self.type_of_event_repo = type_of_event_repo

    def create_type_of_event(self, type_of_event):
        return self.type_of_event_repo.create_type_of_event(type_of_event)

    def get_type_of_event(self, event_id):
        return self.type_of_event_repo.get_type_of_event(event_id)

    def get_all_type_of_events(self):
        return self.type_of_event_repo.get_all_type_of_events()

    def update_type_of_event(self, change):
        return self.type_of_event_repo.update_type_of_event(change)

    def delete_type_of_event(self, event_id):
        return self.type_of_event_repo.delete_type_of_event(event_id)
