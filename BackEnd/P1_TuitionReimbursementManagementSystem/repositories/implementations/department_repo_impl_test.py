import unittest

from models.department import Department
from repositories.implementations.department_repo_impl import DepartmentRepoImpl

dr = DepartmentRepoImpl()


class DepartmentRepoImplTest(unittest.TestCase):

    def test_get_department_success(self):
        dep = dr.get_department(1)
        self.assertEqual(dep, Department(1, 'finance', 7) )
        deps = dr.get_all_departments()
        self.assertEqual(len(deps), 8)


if __name__ == '__main__':
    unittest.main()
