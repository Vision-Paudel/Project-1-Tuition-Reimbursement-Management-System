class Department:

    def __init__(self, department_id: int, department_name: str, department_head: int):
        self.department_id = department_id
        self.department_name = department_name
        self.department_head = department_head

    def __repr__(self):
        return str({
            'department_id': self.department_id,
            'department_name': self.department_name,
            'department_head': self.department_head
        })

    def json(self):
        return {
            'departmentId': self.department_id,
            'departmentName': self.department_name,
            'departmentHead': self.department_head
        }

    def __eq__(self, other):
        if not other:
            return False

        if not isinstance(other, Department):
            return False

        # for value1, value2 in zip(vars(self).values(), vars(other).values()):
        #     if value1 != value2:
        #         return False

        return self.__dict__ == other.__dict__

        return True

