from nameko.rpc import rpc
from dependencies import database

class BenefitService:

    name = 'benefit_service'

    database = database.DatabaseProvider()
    
    ### CRUD TEMPLATE ###
    ### Feel free to remove or make changes ###

    @rpc
    def get_all_benefit(self): #pengecekan ketersediaan data benefit
        benefit_types = self.database.get_all_benefit()
        return benefit_types
    
    @rpc
    def get_benefit_by_id(self, benefit_id): #cek ketersediaan benefit berdasarkan id
        benefits = self.database.get_benefit_by_id(benefit_id)
        return benefits
    
    # @rpc
    # def get_room_type_by_name(self, name):
    #     room_type = self.database.get_room_type_by_name(name)
    #     return room_type
    
    @rpc
    def benefit_data_entry(self, name, description, point_required,discount,start_date,end_date): #data entry benefit
        data = self.database.benefit_data_entry(name, description, point_required,discount,start_date,end_date)
        return data
        
    @rpc
    def edit_benefit_data(self,id, name, description, point_required, discount,start_date,end_date):  #edit data benefit berdasarkan id
        benefits=self.database.edit_benefit_data(id, name, description, point_required, discount,start_date,end_date)
        return benefits
        
    # @rpc
    # def delete_room_type(self, id):
    #     self.database.delete_room_type(id)
    
    ### START YOUR CODE HERE ###

    ### ...

    ### END YOUR CODE HERE ###