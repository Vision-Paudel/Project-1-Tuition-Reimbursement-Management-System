from repositories.interfaces.event_grading_format_repo import EventGradingFormatRepo


class EventGradingFormatService:

    def __init__(self, event_grading_format_repo: EventGradingFormatRepo):
        self.event_grading_format_repo = event_grading_format_repo

    def create_event_grading_format(self, event_grading_format):
        return self.event_grading_format_repo.create_event_grading_format(event_grading_format)

    def get_event_grading_format(self, event_grading_format_id):
        return self.event_grading_format_repo.get_event_grading_format(event_grading_format_id)

    def get_all_event_grading_formats(self):
        return self.event_grading_format_repo.get_all_event_grading_formats()

    def update_event_grading_format(self, event_grading_format):
        return self.event_grading_format_repo.update_event_grading_format(event_grading_format)

    def delete_event_grading_format(self, event_grading_format_id):
        return self.event_grading_format_repo.delete_event_grading_format(event_grading_format_id)
