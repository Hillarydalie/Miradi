import unittest
from app.models import Project, User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("UN", "Hospital-Construction", "community-health" )

    def test_init(self):
        self.assertEqual(self.new_user_username, "UN")
        self.assertEqual(self.new_user_project, "Hospital-Construction")
        self.assertEqual(self.new_user_comments, 'community-health')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    user_list = []
    def save_user(self):
        User.user_list.append(self)


    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Test", "user", "email@user.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.contact_list))

        def delete_contact(self):
            User.user_list.remove(self)


        def test_find_user_by_username(self):
            self.new_user.save_user()
            test_user = User("Test", "user", "email@user.com")
            test_user.save_user()

            found_user = User.find_by_username("Test")
            self.assertEqual(found_user.email, test_user.email)





class TestProject(unittest.TestCase):
    def setUp(self):
        self.new_project = Project("Hospital-Construction", "community-health")
        

    def test_init(self):
        self.assertEqual(self.new_project_name, "Hospital-Construction")
        self.assertEqual(self.new_project_description, "community-health")



if __name__ == '__main__':
    unittest.main()