from flask import request, jsonify

from exceptions.resource_not_created import ResourceNotCreated
from exceptions.resource_not_found import ResourceNotFound
from models.register_user_details_from_frontend import RegisterUserDetailsFromFrontEnd
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

    @app.route("/register", methods=['POST'])
    def register():
        body = request.json
        rud = RegisterUserDetailsFromFrontEnd(username=body["username"],password=body["password"],email=body["email"],
                                              employee_id=body["employeeId"])
        try:
            try:
                eudr.get_employee_user_details_by_employee_id(body["employeeId"])
                return "Employee user detail already exists! Contact IT for user details!", 404
            except ResourceNotFound as rnf:
                new_eud = eudr.create_employee_user_details(register_details=rud)
                return jsonify(new_eud.json()), 201
        except ResourceNotCreated as rnc:
            return rnc.message, 404


