from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.tuition_reimbursement_form_data import TuitionReimbursementFormData
from repositories.interfaces.tuition_reimbursement_form_data_repo import TuitionReimbursementFormDataRepo
from util.db_connection import connection


def _build_tuition_reimbursement_form_data(record):
    return TuitionReimbursementFormData(tuition_reimbursement_form_data_id=record[0], attending_employee=record[1],
                                        event_date_time=record[2], event_location=record[3],
                                        event_description=record[4],
                                        event_cost=record[5], event_grading_format=record[6], type_of_event=record[7]
                                        )


class TuitionReimbursementFormDataRepoImpl(TuitionReimbursementFormDataRepo):

    def create_tuition_reimbursement_form_data(self, tuition_reimbursement_form_data: TuitionReimbursementFormData,
                                               event_related_attachment=None, approvals_already_provided=None):
        # Struture: tuition_reimbursement_form_data_id: int, attending_employee: int, event_date_time,
        #           event_location, event_description, event_cost, event_grading_format, type_of_event,
        #           event_related_attachment = None, approvals_already_provided = None
        sql = "INSERT INTO tuition_reimbursement_form_data VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [tuition_reimbursement_form_data.attending_employee,
                             tuition_reimbursement_form_data.event_date_time, tuition_reimbursement_form_data.event_location,
                             tuition_reimbursement_form_data.event_description, tuition_reimbursement_form_data.event_cost,
                             int(tuition_reimbursement_form_data.event_grading_format), int(tuition_reimbursement_form_data.type_of_event)])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_form_data(record)
        else:
            raise ResourceNotCreated("Tuition reimbursement form data was not created. Check logs!")

    def get_tuition_reimbursement_form_data(self, tuition_reimbursement_form_data_id):
        sql = "SELECT * FROM tuition_reimbursement_form_data WHERE tuition_reimbursement_form_data_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [tuition_reimbursement_form_data_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_tuition_reimbursement_form_data(record)
        else:
            raise ResourceNotFound(f"Tuition form with id {tuition_reimbursement_form_data_id} not found!")

    def get_all_tuition_reimbursement_form_data(self):
        sql = "SELECT * FROM tuition_reimbursement_form_data"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        tuition_form_list = [_build_tuition_reimbursement_form_data(record) for record in records]

        return tuition_form_list

    def get_all_tuition_reimbursement_form_data_by_employee(self, employee_id):
        sql = "SELECT * FROM tuition_reimbursement_form_data WHERE attending_employee=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        records = cursor.fetchall()

        tuition_form_list = [_build_tuition_reimbursement_form_data(record) for record in records]

        return tuition_form_list

    def update_tuition_reimbursement_form_data(self, change: TuitionReimbursementFormData,
                                               event_related_attachment=None,
                                               approvals_already_provided=None):
        # employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int, department: int
        sql = "UPDATE tuition_reimbursement_form_data SET attending_employee=%s, event_date_time=%s, " \
              "event_location=%s, event_description=%s, event_cost=%s, event_grading_format=%s, type_of_event=%s, " \
              "WHERE tuition_reimbursement_form_data_id=%s" \
              " RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.attending_employee, change.event_date_time, change.event_location,
                             change.event_description, change.event_cost, change.event_grading_format,
                             change.type_of_event])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_form_data(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update tuition_reimbursement_form_data with id {change.employee_id}. Check logs!")

    def delete_event_grading_format(self, tuition_reimbursement_form_data_id):
        sql = "DELETE FROM tuition_reimbursement_form_data WHERE tuition_reimbursement_form_data_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [tuition_reimbursement_form_data_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_form_data(record)
        else:
            form_id = tuition_reimbursement_form_data_id
            raise ResourceNotDeleted(f"Cannot delete tuition reimbursement form data with id {form_id}. Check logs!")
