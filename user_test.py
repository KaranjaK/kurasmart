import unittest 
from user import User



class Testuser(unittest.TestCase):
    def setUp(self):
         self.new_user = User("Carolyne","mamu234","36777")
    

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "Carolyne")
        
        self.assertEqual(self.new_user.password, "mamu234")

        self.assertEqual(self.new_user.id_number, "36777")
        
   
    def test_save_user(self):
        """
        test_save_user test used to test if the user object  has been saved in the user list 
        """
        self.new_user.save_user() # use for saving new contact
        self.assertEqual(len(User.userlist),2)
   

    def test_delete_user(self):
        """
        test delete  is used to test if the contact can be deleted from the contact list
        """
        self.new_user.save_user()
        test_user = User("Carolyne","mamu234","36777") 
        test_user.save_user()

        self.new_user.delete_user() 
        self.assertEqual(len(User.userlist),1)
  


if __name__== '__main__':
    unittest.main()