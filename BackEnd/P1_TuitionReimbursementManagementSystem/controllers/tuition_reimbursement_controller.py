
from flask import request, jsonify

from exceptions.resource_not_created import ResourceNotCreated
from models.tuition_reimbursement_form_data import TuitionReimbursementFormData
from models.tuition_reimbursement_process import TuitionReimbursementProcess
from repositories.implementations.tuition_reimbursement_form_data_repo_impl import TuitionReimbursementFormDataRepoImpl
from repositories.implementations.tuition_reimbursement_process_repo_impl import TuitionReimbursementProcessRepoImpl
from repositories.interfaces.tuition_reimbursement_form_data_repo import TuitionReimbursementFormDataRepo
from repositories.interfaces.tuition_reimbursement_process_repo import TuitionReimbursementProcessRepo
from services.tuition_reimbursement_form_data_service import TuitionReimbursementFormDataService
from services.tuition_reimbursement_process_service import TuitionReimbursementProcessService

trfdr: TuitionReimbursementFormDataRepo = TuitionReimbursementFormDataRepoImpl
trfds: TuitionReimbursementFormDataService = TuitionReimbursementFormDataService(trfdr)
trpr: TuitionReimbursementProcessRepo = TuitionReimbursementProcessRepoImpl()
trps: TuitionReimbursementProcessService = TuitionReimbursementProcessService(trpr);

def route(app):

    @app.route("/tuition_reimbursement_form", methods=['POST'])
    def post_a_new_claim():
        body = request.json
        try:
            print(body["attendingEmployee"])
            tfd = TuitionReimbursementFormData(tuition_reimbursement_form_data_id=body["tuitionReimbursementFormDataId"],
                                        attending_employee=body["attendingEmployee"],event_date_time=body["eventDateTime"],
                                         event_location=body["location"], event_description=body["description"],
                                         event_cost=body["eventCost"], event_grading_format=body["eventGradingFormat"],
                                         type_of_event=body["typeOfEvent"])
            newtfd: TuitionReimbursementFormData = trfds.create_tuition_reimbursement_form_data(tfd)
            newtfp = trps.create_tuition_reimbursement_process(TuitionReimbursementProcess(newtfd.tuition_reimbursement_form_data_id))
            return jsonify(newtfp.json()), 200;
        except ResourceNotCreated as rnc:
            return rnc.message, 500

    @app.route("/tuition_reimbursement_form/<employee_id>", methods=['GET'])
    def get_all_claims_by_id(employee_id):
        newtfds: TuitionReimbursementFormData = trfds.get_all_tuition_reimbursement_form_data_by_employee(employee_id)
        return jsonify([tfd.json() for tfd in newtfds]), 200

    @app.route("/tuition_reimbursement_form/<tuition_reimbursement_form_id>", methods=['GET'])
    def update_tuition_reimbursement_form_process(tuition_reimbursement_form_id):
        body = request.json
        return 200;
