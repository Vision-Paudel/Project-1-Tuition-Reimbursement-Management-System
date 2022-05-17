import random

from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_deleted import ResourceNotDeleted
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_updated import ResourceNotUpdated
from models.register_user_details_from_frontend import RegisterUserDetailsFromFrontEnd
from models.employee_user_details_from_frontend import EmployeeUserDetailsFromFrontend
from models.employee_user_details import EmployeeUserDetails
from repositories.interfaces.employee_user_details_repo import EmployeeUserDetailsRepo
from util.db_connection import connection
import hashlib
import uuid
from datetime import datetime


def _build_employee_user_details(record):
    return EmployeeUserDetails(record[0], record[1], record[2], record[3], record[4], record[5], record[6])


class EmployeeUserDetailsRepoImpl(EmployeeUserDetailsRepo):

    @staticmethod
    def gen_random_salt(length: int):
        string_to_return: str = ""
        r = random.SystemRandom()

        for n in range(0, length):
            random_integer = r.randint(a=0, b=2)
            if random_integer == 0:
                random_integer = r.randint(48, 57)
                string_to_return += chr(random_integer)
            elif random_integer == 1:
                random_integer = r.randint(65, 90)
                string_to_return += chr(random_integer)
            else:
                random_integer = r.randint(97, 122)
                string_to_return += chr(random_integer)

        return string_to_return

    def create_employee_user_details(self, register_details: RegisterUserDetailsFromFrontEnd):
        # employee_user_details structure: username, password_hash, salt, email, security_token,
        # last_successful_log_in, employee_id
        # register_details structure: username, password, email, employee_id
        try:
            exists = self.get_employee_user_details_by_employee_id(register_details.employee_id)
        except ResourceNotFound as rnf:
            sql = "INSERT INTO employee_user_details VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
            from util.db_connection import connection
            cursor = connection.cursor()

            salt: str = EmployeeUserDetailsRepoImpl.gen_random_salt(12)
            password_hash: str = hashlib.sha512((salt + register_details.password).encode('utf-8')).hexdigest()
            security_token = uuid.uuid4()
            cursor.execute(sql, [register_details.username, password_hash, salt, register_details.email,
                                 str(security_token), None, register_details.employee_id])

            connection.commit()
            record = cursor.fetchone()
            if record is not None:
                return _build_employee_user_details(record)
            else:
                raise ResourceNotCreated("Employee user details was not created. Check logs!")

    def get_employee_user_details_by_username(self, username):
        # employee_user_details structure: username, password_hash, salt, email, security_token,
        # last_successful_log_in, employee_id
        sql = "SELECT * FROM employee_user_details WHERE username=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [username])

        record = cursor.fetchone()

        if record is not None:
            return _build_employee_user_details(record)
        else:
            raise ResourceNotFound(f"Employee with employee id {username} not found!")

    def get_employee_user_details_by_employee_id(self, employee_id):
        # employee_user_details structure: username, password_hash, salt, email, security_token,
        # last_successful_log_in, employee_id
        sql = "SELECT * FROM employee_user_details WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        if record is not None:
            return _build_employee_user_details(record)
        else:
            raise ResourceNotFound(f"Employee with employee id {employee_id} not found!")

    def get_all_employee_user_details(self):
        # employee_user_details structure: username, password_hash, salt, email, security_token,
        # last_successful_log_in, employee_id
        sql = "SELECT * FROM employee_user_details"

        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        employee_details_list = [_build_employee_user_details(record) for record in records]

        return employee_details_list

    def update_employee_user_details(self, employee_user_details_from_frontend: EmployeeUserDetailsFromFrontend):
        # employee_user_details structure: username, password_hash, salt, email, security_token,
        # last_successful_log_in, employee_id
        # employee_user_details_from_frontend structure: username, password, email, security_token,
        # last_successful_log_in, employee_id
        sql = "UPDATE employee_user_details SET username=%s, password_hash=%s, salt=%s, email=%s, security_token=%s," \
              " last_successful_log_in=%s, WHERE employee_id=%s RETURNING *"

        cursor = connection.cursor()

        salt: str = EmployeeUserDetailsRepoImpl.gen_random_salt(12)
        password_hash: str = hashlib.sha512((salt + employee_user_details_from_frontend.password).encode('utf-8')).hexdigest()

        cursor.execute(sql,
                       [employee_user_details_from_frontend.username, password_hash, salt,
                        employee_user_details_from_frontend.email, employee_user_details_from_frontend.security_token,
                        employee_user_details_from_frontend.employee_id])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_employee_user_details(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update employee user details of employee with id "
                f"{employee_user_details_from_frontend.employee_id}. Check logs!")

    def set_new_last_successful_log_in_for_employee_details(self, username):
        sql = "UPDATE employee_user_details SET last_successful_log_in=%s WHERE username=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [int(datetime.now().timestamp()), username])
        record = cursor.fetchone()
        if record is not None:
            return _build_employee_user_details(record)
        else:
            raise ResourceNotUpdated(
                f"Cannot update employee user details of employee with username {username}. Check logs!")

    def delete_employee_user_details(self, username):
        sql = "DELETE FROM employee_user_details WHERE username=%s  RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [username])

        connection.commit()
        record = cursor.fetchone()
        if record is not None:
            return _build_employee_user_details(record)
        else:
            raise ResourceNotDeleted(f"Cannot delete employee with username {username}. Check logs!")


