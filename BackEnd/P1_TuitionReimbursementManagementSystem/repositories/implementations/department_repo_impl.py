from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.department import Department
from repositories.interfaces.department_repo import DepartmentRepo
from util.db_connection import connection


def _build_department(record):
    return Department(department_id=record[0], department_name=record[1], department_head=record[2])


class DepartmentRepoImpl(DepartmentRepo):

    def create_department(self, department: Department):
        # department_id: int, department_name: str, department_head: int
        sql = "INSERT INTO department VALUES (DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [department.department_name, department.department_head])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_department(record)
        else:
            raise ResourceNotCreated("Department was not created. Check logs!")

    def get_department(self, department_id):
        # department_id: int, department_name: str, department_head: int
        sql = "SELECT * FROM department WHERE department_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [department_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_department(record)
        else:
            raise ResourceNotFound(f"Department with department id {department_id} not found!")

    def get_all_departments(self):
        # department_id: int, department_name: str, department_head: int
        sql = "SELECT * FROM department"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        department_list = [_build_department(record) for record in records]

        return department_list

    def update_department(self, change: Department):
        # department_id: int, department_name: str, department_head: int
        sql = "UPDATE department SET department_name=%s, department_head=%s" \
              "WHERE department_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.department_name, change.department_head, change.department_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_department(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update department with department id {change.department_id}. Check logs!")

    def delete_department(self, department_id):
        sql = "DELETE FROM department WHERE department_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [department_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_department(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete department with department id {department_id}. Check logs!")
