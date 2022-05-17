import hashlib

from flask import request, jsonify
from exceptions.invalid_login import InvalidLogin
from exceptions.resource_not_found import ResourceNotFound
from models.employee_user_details import EmployeeUserDetails
from repositories.implementations.employee_repo_impl import EmployeeRepoImpl
from repositories.implementations.employee_user_details_repo_impl import EmployeeUserDetailsRepoImpl
from repositories.interfaces.employee_user_details_repo import EmployeeUserDetailsRepo
from services.employee_service import EmployeeServiceImpl
from services.employee_user_details_service import EmployeeUserDetailsService


employee_repo = EmployeeRepoImpl()
employee_service = EmployeeServiceImpl(employee_repo)
eudr: EmployeeUserDetailsRepo = EmployeeUserDetailsRepoImpl()
euds: EmployeeUserDetailsService = EmployeeUserDetailsService(eudr)


def route(app):

    @app.route("/login", methods=['POST'])
    def login():
        body = request.json
        try:
            employee_user_details_obj: EmployeeUserDetails = eudr.get_employee_user_details_by_username(body["username"])

            real_user_password_hash = employee_user_details_obj.password_hash
            input_password_hash = hashlib.sha512((employee_user_details_obj.salt + body["password"]).encode('utf-8')).hexdigest()

            if real_user_password_hash == input_password_hash:
                eudr.set_new_last_successful_log_in_for_employee_details(body["username"])
                return jsonify(employee_user_details_obj.json()), 200
            else:
                raise InvalidLogin("Invalid Login Details!")

        except ResourceNotFound as rnf:
            return rnf.message, 404
        except InvalidLogin as invlogin:
            return invlogin.message, 404
