import unittest

from repositories.implementations.employee_user_details_repo_impl import EmployeeUserDetailsRepoImpl

er = EmployeeUserDetailsRepoImpl()


class EmployeeUserDetailsRepoImpl(unittest.TestCase):

    def test_get_employee_success(self):
        pass

if __name__ == '__main__':
    unittest.main()