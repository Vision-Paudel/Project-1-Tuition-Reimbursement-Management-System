from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.employee import Employee
from repositories.interfaces.employee_repo import EmployeeRepo
from util.db_connection import connection


def _build_employee(record):
    return Employee(employee_id=record[0], first_name=record[1], last_name=record[2], job_title=record[3],
                    supervisor=record[4], department=record[5])


class EmployeeRepoImpl(EmployeeRepo):

    def create_employee(self, employee: Employee):
        # employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int, department: int
        sql = "INSERT INTO employee VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()

        cursor.execute(sql, [employee.first_name, employee.last_name, employee.job_title, employee.supervisor,
                             employee.department])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_employee(record)
        else:
            raise ResourceNotCreated("Employee was not created. Check logs!")

    def get_employee(self, employee_id):
        # employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int, department: int
        sql = "SELECT * FROM employee WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_employee(record)
        else:
            raise ResourceNotFound(f"Employee with employee id {employee_id} not found!")

    def get_all_employees(self):
        # employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int, department: int
        sql = "SELECT * FROM employee"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        employee_list = [_build_employee(record) for record in records]

        return employee_list

    def update_employee(self, change: Employee):
        # employee_id: int, first_name: str, last_name: str, job_title: str, supervisor: int, department: int
        sql = "UPDATE employee SET first_name=%s, last_name=%s, job_title=%s, supervisor=%s, department=%s" \
              "WHERE employee_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.first_name, change.last_name, change.job_title, change.supervisor, change.department,
                             change.employee_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_employee(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update employee with employee id {change.employee_id}. Check logs!")

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employee WHERE employee_id=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_employee(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete employee with employee id {employee_id}. Check logs!")
