from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.tuition_reimbursement_process import TuitionReimbursementProcess
from repositories.interfaces.tuition_reimbursement_process_repo import TuitionReimbursementProcessRepo
from util.db_connection import connection


def _build_tuition_reimbursement_process(record):
    return TuitionReimbursementProcess(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                       record[7])


class TuitionReimbursementProcessRepoImpl(TuitionReimbursementProcessRepo):
    def create_tuition_reimbursement_process(self, tuition_reimbursement_process: TuitionReimbursementProcess):
        # tr_form_data_id, approved_by_supervisor, approved_by_department_head,
        # approved_by_benefits_coordinator, presented, grade_received, confirmed, reimbursed
        sql = "INSERT INTO tuition_reimbursement_process VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [tuition_reimbursement_process.tr_form_data_id,
                             tuition_reimbursement_process.approved_by_supervisor,
                             tuition_reimbursement_process.approved_by_department_head,
                             tuition_reimbursement_process.approved_by_benefits_coordinator,
                             tuition_reimbursement_process.presented, tuition_reimbursement_process.grade_received,
                             tuition_reimbursement_process.confirmed, tuition_reimbursement_process.reimbursed])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_process(record)
        else:
            raise ResourceNotCreated("Tuition reimbursement form process was not created. Check logs!")

    def get_tuition_reimbursement_process(self, tr_form_data_id):
        sql = "SELECT * FROM tuition_reimbursement_process WHERE tr_form_data_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [tr_form_data_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_tuition_reimbursement_process(record)
        else:
            raise ResourceNotFound(f"Tuition form with id {tr_form_data_id} not found!")

    def get_all_tuition_reimbursement_process(self):
        sql = "SELECT * FROM tuition_reimbursement_process"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        tuition_form_process_list = [_build_tuition_reimbursement_process(record) for record in records]

        return tuition_form_process_list

    def update_tuition_reimbursement_process(self, change: TuitionReimbursementProcess):
        sql = "UPDATE tuition_reimbursement_process SET approved_by_supervisor=%s, approved_by_department_head=%s, " \
              "approved_by_benefits_coordinator=%s, presented=%s, grade_received=%s, confirmed=%s, reimbursed=%s " \
              "WHERE tr_form_data_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [change.approved_by_supervisor, change.approved_by_department_head,
                             change.approved_by_benefits_coordinator,
                             change.presented, change.grade_received, change.confirmed,
                             change.reimbursed, change.tr_form_data_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_process(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update tuition_reimbursement_process with id {change.tr_form_data_id}. Check logs!")

    def delete_reimbursement_process(self, tr_form_data_id):
        sql = "DELETE FROM tuition_reimbursement_process WHERE tr_form_data_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [tr_form_data_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_tuition_reimbursement_process(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete tuition reimbursement process with form_id {tr_form_data_id}. Check logs!")
