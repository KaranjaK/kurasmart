class User :
   
   userlist = []
   def __init__(self,user_name,password,id_number):
       self.user_name = user_name
       self.password = password
       self.id_number = id_number

   def  save_user(self):
    
        User.userlist.append(self)
   
   def delete_user(self):# delete method deletes saved user from the userlist
         
       User.userlist.remove(self)

   @classmethod
   def display_users(cls):
       return cls.userlist


   @classmethod
   def find_by_number(cls,phonenumber):

       for user in cls.userlist:
           if user.id_number== id:
               return True

#    @classmethod
#    def clear_all(cls):
#        if(len(cls.userlist) == 0):
#                 return "Empty"
       else:
            for user in cls.userlist:
                cls.userlist.remove(user)

