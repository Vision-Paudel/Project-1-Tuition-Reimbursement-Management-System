from flask import jsonify

from repositories.implementations.event_grading_format_repo_impl import EventGradingFormatRepoImpl
from repositories.interfaces.event_grading_format_repo import EventGradingFormatRepo
from services.event_grading_format_service import EventGradingFormatService

er: EventGradingFormatRepo = EventGradingFormatRepoImpl()
es: EventGradingFormatService = EventGradingFormatService(er);

def route(app):

    @app.route("/event_grading_format", methods=['GET'])
    def get_event_grading_format():
        evgs = es.get_all_event_grading_formats()
        return jsonify([evg.json() for evg in evgs]), 200