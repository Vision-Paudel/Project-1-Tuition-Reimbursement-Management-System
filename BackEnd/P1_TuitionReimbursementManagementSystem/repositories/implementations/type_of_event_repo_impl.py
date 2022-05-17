from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.type_of_event import TypeOfEvent
from repositories.interfaces.type_of_event_repo import TypeOfEventRepo
from util.db_connection import connection


def _build_type_of_event(record):
    return TypeOfEvent(record[0], record[1], record[2])


class TypeOfEventRepoImpl(TypeOfEventRepo):

    def create_type_of_event(self, type_of_event: TypeOfEvent):
        # event_id, event_type, reimbursement_amount
        sql = "INSERT INTO type_of_event VALUES (DEFAULT, %s, %s ) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [type_of_event.event_type, type_of_event.reimbursement_amount])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_type_of_event(record)
        else:
            raise ResourceNotCreated("Type of event was not created. Check logs!")

    def get_type_of_event(self, event_id):
        sql = "SELECT * FROM type_of_event WHERE event_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [event_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_type_of_event(record)
        else:
            raise ResourceNotFound(f"Type of event id {event_id} not found!")

    def get_all_type_of_events(self):
        sql = "SELECT * FROM type_of_event"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        type_of_event_list = [_build_type_of_event(record) for record in records]

        return type_of_event_list

    def update_type_of_event(self, change: TypeOfEvent):
        sql = "UPDATE type_of_event SET event_type=%s, reimbursement_amount=%s, WHERE event_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.event_type, change.reimbursement_amount, change.event_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_type_of_event(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update type_of_event with id {change.event_id}. Check logs!")

    def delete_type_of_event(self, event_id):
        sql = "DELETE FROM type_of_event WHERE event_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [event_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_type_of_event(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete type of event with id {event_id}. Check logs!")
