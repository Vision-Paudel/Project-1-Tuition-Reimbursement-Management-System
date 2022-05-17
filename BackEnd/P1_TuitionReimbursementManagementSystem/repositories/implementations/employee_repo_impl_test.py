import unittest

from models.employee import Employee
from repositories.implementations.employee_repo_impl import EmployeeRepoImpl

er = EmployeeRepoImpl()


class EmployeeRepoImplTest(unittest.TestCase):

    def test_get_employee_success(self):
        emp = er.get_employee(1)
        self.assertEqual(emp, Employee(1, 'Homer','Simpson', 'CEO, Department Head - Executive', None, 2) )
        emps = er.get_all_employees()
        self.assertEqual(len(emps), 8)

if __name__ == '__main__':
    unittest.main()
