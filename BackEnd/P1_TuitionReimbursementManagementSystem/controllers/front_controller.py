from controllers import login_controller, tuition_reimbursement_controller, register_controller, department_controller, \
    employee_controller


def route(app):
    # Call all other controllers
    register_controller.route(app)
    login_controller.route(app)
    tuition_reimbursement_controller.route(app)
    department_controller.route(app)
    employee_controller.route(app)