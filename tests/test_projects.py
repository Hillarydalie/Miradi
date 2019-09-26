import unittest
from app.models import Project



class TestProject(unittest.TestCase):
    def setUp(self):
        self.new_project = Project("Hospital-Construction", "community-health")
        

    def test_init(self):
        self.assertEqual(self.new_project_name, "Hospital-Construction")
        self.assertEqual(self.new_project_description, "community-health")



if __name__ == '__main__':
    unittest.main()