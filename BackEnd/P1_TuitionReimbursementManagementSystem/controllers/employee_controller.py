from flask import jsonify

from repositories.implementations.employee_repo_impl import EmployeeRepoImpl
from repositories.interfaces.employee_repo import EmployeeRepo
from services.employee_service import EmployeeServiceImpl

er: EmployeeRepo = EmployeeRepoImpl()
es: EmployeeServiceImpl = EmployeeServiceImpl(er);

def route(app):

    @app.route("/employees", methods=['GET'])
    def get_employees():
        employees = es.get_all_employees()
        return jsonify([emp.json() for emp in employees]), 200