from flask import jsonify

from repositories.implementations.department_repo_impl import DepartmentRepoImpl
from repositories.interfaces.department_repo import DepartmentRepo
from services.department_service import DepartmentServiceImpl

dr: DepartmentRepo = DepartmentRepoImpl()
ds: DepartmentServiceImpl = DepartmentServiceImpl(dr);

def route(app):

    @app.route("/departments", methods=['GET'])
    def get_departments():
        departments = ds.get_all_departments()
        return jsonify([dep.json() for dep in departments]), 200