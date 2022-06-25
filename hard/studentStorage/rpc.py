from nameko.rpc import rpc
import database

class StudentService:

    name = 'user_service'

    database = database.DatabaseProvider()

    @rpc
    def register_data(self, nrp, nama, email,password): #data entry student
        data = self.database.register_data(nrp, nama, email,password)
        return data

    @rpc
    def get_id(self,email,password):
        id=self.database.get_id(email,password)
        return id

    @rpc
    def upload_file(self, nrp, file):
        self.database.upload_file(nrp, file) 