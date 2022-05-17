class EventGradingFormat:

    def __init__(self, event_grading_format_id, grade_format_type, passing_grade):
        self.event_grading_format_id = event_grading_format_id
        self.grade_format_type = grade_format_type
        self.passing_grade = passing_grade

    def __repr__(self):
        return str({
            'event_grading_format_id': self.event_grading_format_id,
            'grade_format_type': self.grade_format_type,
            'passing_grade': self.passing_grade
        })

    def json(self):
        return {
            'eventGradingFormatId': self.event_grading_format_id,
            'gradeFormatType': self.grade_format_type,
            'passingGrade': self.passing_grade
        }
