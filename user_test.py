import unittest 
from user import Management, User


class Testuser(unittest.TestCase):
    def setUp(self):
         self.new_user = User("Rose","wikiki","36777")
    

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Rose")
        
        self.assertEqual(self.new_user.password, "wikiki")

        self.assertEqual(self.new_user.id_number, "36777")
        
   
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.userlist),2)
   

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Rose","wikiki","36777") 
        test_user.save_user()

        self.new_user.delete_user() 
        self.assertEqual(len(User.userlist),1)
  

class Testmanagement(unittest.TestCase):
    def setUp(self):
         self.new_management = Management("David","bright","3444")
    

    def test_init(self):
        self.assertEqual(self.new_management.management_name, "David")
        
        self.assertEqual(self.new_management.password, "bright")

        self.assertEqual(self.new_management.id_number, "3444")
        
   
    def test_save_management(self):
        self.new_management.save_management()
        self.assertEqual(len(Management.managementlist),2)
   

    def test_delete_managment(self):
        self.new_management.save_management()
        test_management = Management("David","bright","3444") 
        test_management.save_management()

        self.new_management.delete_management() 
        self.assertEqual(len(Management.managementlist),1)
  


if __name__== '__main__':
    unittest.main()