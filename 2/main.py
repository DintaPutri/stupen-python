class data():
    def __init__(self,name,username):
        self.__name = name
        self.__username = username
        
    def get_name(self):
        return self.__name
    
    def set_name(self, nama_baru):
         self.__name = nama_baru

    def get_username(self):
        return self.__username
    
    def set_username(self, username_baru):
         self.__username = username_baru
         
Data = data("Ditna", "ptr")

print("Nama : ", Data.get_name())
print("Username : ", Data.get_username())

Data.set_name("Dinta Putri")
Data.set_username("Puput")

print("Nama Setelah Perubahan:", Data.get_name()) 
print("Username Setelah Perubahan:", Data.get_username())     