class User :
   
   userlist = []
   def __init__(self,user_name,password,id_number):
       self.user_name = user_name
       self.password = password
       self.id_number = id_number

   def  save_user(self):
    
        User.userlist.append(self)
   
   def delete_user(self):
         
       User.userlist.remove(self)

   @classmethod
   def display_users(cls):
       return cls.userlist


   @classmethod
   def find_by_id_number(cls,id_number):

       for user in cls.userlist:
           if user.id_number== id:
               return True

       else:
            for user in cls.userlist:
                cls.userlist.remove(user)


class Management:
   
   managementlist = []
   def __init__(self,management_name,password,id_number):
       self.management_name = management_name
       self.password = password
       self.id_number = id_number

   def  save_management(self):
    
        Management.managementlist.append(self)
   
   def delete_management(self):
         
       Management.managementlist.remove(self)

   @classmethod
   def display_management(cls):
       return cls.managementlist


   @classmethod
   def find_by_id_number(cls,id_number):

       for management in cls.managementlist:
           if management.id_number== id:
               return True
       else:
            for management in cls.managementlist:
                cls.managementlist.remove(management)
