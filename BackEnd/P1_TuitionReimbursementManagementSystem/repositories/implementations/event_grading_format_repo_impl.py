from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.event_grading_format import EventGradingFormat
from repositories.interfaces.event_grading_format_repo import EventGradingFormatRepo
from util.db_connection import connection


def _build_event_grading_format(record):
    return EventGradingFormat(record[0], record[1], record[2])


class EventGradingFormatRepoImpl(EventGradingFormatRepo):

    def create_event_grading_format(self, event_grading_format: EventGradingFormat):
        # event_grading_format_id, grade_format_type, passing_grade
        sql = "INSERT INTO event_grading_format VALUES (DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [event_grading_format.grade_format_type, event_grading_format.passing_grade])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_event_grading_format(record)
        else:
            raise ResourceNotCreated("Event Grading format was not created. Check logs!")

    def get_event_grading_format(self, event_grading_format_id):
        # event_grading_format_id, grade_format_type, passing_grade
        sql = "SELECT * FROM event_grading_format WHERE event_grading_format_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [event_grading_format_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_event_grading_format(record)
        else:
            raise ResourceNotFound(
                f"Event grading format with event grading format id {event_grading_format_id} not found!")

    def get_all_event_grading_formats(self):
        # event_grading_format_id, grade_format_type, passing_grade
        sql = "SELECT * FROM event_grading_format"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        event_grading_format_list = [_build_event_grading_format(record) for record in records]

        return event_grading_format_list

    def update_event_grading_format(self, change: EventGradingFormat):
        # event_grading_format_id, grade_format_type, passing_grade
        sql = "UPDATE event_grading_format SET grade_format_type=%s, passing_grade=%s" \
              "WHERE event_grading_format_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.grade_format_type, change.passing_grade, change.event_grading_format_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_event_grading_format(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update grade format type with id {change.event_grading_format_id}. Check logs!")

    def delete_event_grading_format(self, event_grading_format_id):
        sql = "DELETE FROM event_grading_format WHERE event_grading_format_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [event_grading_format_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_event_grading_format(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete grade format type with id {event_grading_format_id}. Check logs!")
