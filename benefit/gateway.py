import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from werkzeug.wrappers import Response
from service import BenefitService
from dependencies.redis import SessionProvider

class BenefitGatewayService:
    name = 'benefit_gateway'
    benefit_rpc = RpcProxy('benefit_service')
    #session intialized
    session_provider=SessionProvider()

    @http('GET', '/api/benefit')
    def fetch_data_benefit(self, request):
        benefit = self.benefit_rpc.get_all_benefit()
        
        #session
        # cookies=request.cookies
        # session_id = self.session_provider.set_session_data(benefit)
        # if cookies:
        #     session_data = self.session_provider.get_session_data(cookies['SESSID'])
        # response = Response(str(benefit))
        # response.set_cookie('SESSID', session_id)
        return Response(json.dumps(benefit), mimetype='application/json')
        # PLEASE CODE WITH SPECIFICATION BELOW
        

        ### RESPONSES
        
        #Fetch Data Benefit
        #BODY: 
        # {
        #     "status": "success",
        #     "data": [
        #         {
        #             "id_benefit": 1,
        #             "name": "Benefit 1",
        #             "description": "all product",
        #             "point_required": 100,
        #             "discount": 10
        #         },
        #         {
        #             "id_benefit": 2,
        #             "name": "Benefit 2",
        #             "description": "all product",
        #             "point_required": 200,
        #             "discount": 20
        #         }
        #     ]
        # }
        # STATUS CODE:
        # OK | 200
        
        pass

    @http('POST', '/api/benefit')
    def benefit_data_entry(self, request):
        data_name = request.get_json()['name']
        data_description=request.get_json()['description']
        data_point_required=request.get_json()['point_required']
        data_discount=request.get_json()['discount']
        data_start=request.get_json()['start_date']
        data_end=request.get_json()['end_date']
        entry=self.benefit_rpc.benefit_data_entry(data_name,data_description,data_point_required,data_discount,data_start,data_end)
        #session
        # cookies=request.cookies
        # session_id = self.session_provider.set_session_data(entry)
        # response = Response(str(entry))
        # response.set_cookie('SESSID', session_id)
        return u"Received: {}".format(request.get_data(as_text=True))
        # PLEASE CODE WITH SPECIFICATION BELOW
        

        ### REQUEST BODY
        {
            "name": "Benefit 1",
            "description": "all product",
            "point_required": 100,
            "discount": 10
        }
        

        ### RESPONSES
        
        # Benefit data entry
        # BODY: 
        {
            "status": "success",
            "message": "Benefit created successfully",
            "data": {
                "id_benefit": 1,
                "name": "Benefit 1",
                "description": "all product",
                "point_required": 100,
                "discount": 10
            }
        }
        # STATUS CODE:
        # Created | 201
        
        pass

    @http('GET', '/api/benefit/<int:benefit_id>')
    def get_benefit_by_id(self, request, benefit_id):
        benefit = self.benefit_rpc.get_benefit_by_id(benefit_id)
        #session
        # cookies=request.cookies
        # session_id = self.session_provider.set_session(benefit)
        # response = Response(str(benefit))
        # response.set_cookie('SESSID', session_id)
        return Response(json.dumps(benefit), mimetype='application/json')
        # PLEASE CODE WITH SPECIFICATION BELOW
        

        ### RESPONSES
        
        # Check the availability of benefits data
        # BODY: 
        {
            "status": "success",
            "data": {
                "id_benefit": 1,
                "name": "Benefit 1",
                "description": "all product",
                "point_required": 100,
                "discount": 10
            }
        }
        # STATUS CODE:
        # OK | 200
        
        # Checking the availability of Benefit not found data
        # BODY: 
        {
            "status": "error",
            "message": "Benefit not found"
        }
        # STATUS CODE:
        # Not Found | 404
        
        pass

    @http('PUT', '/api/benefit/<int:id>')
    def edit_benefit_data(self, request, id):
        data_id = id
        data_name = request.get_json()['name']
        data_description=request.get_json()['description']
        data_point_required=request.get_json()['point_required']
        data_discount=request.get_json()['discount']
        data_start=request.get_json()['start_date']
        data_end=request.get_json()['end_date']
        benefit=self.benefit_rpc.edit_benefit_data(data_id,data_name,data_description,data_point_required,data_discount,data_start,data_end)
        #session
        # cookies=request.cookies
        # session_id = self.session_provider.set_session(benefit)
        # response = Response(str(benefit))
        # response.set_cookie('SESSID', session_id)
        return u"Updated: {}".format(request.get_data(as_text=True))        
        # PLEASE CODE WITH SPECIFICATION BELOW
        

        ### REQUEST BODY
        {
            "name": "Gebyar Diskon",
            "description": "Spesial 11/11",
            "point_required": 150,
            "discount": 20
        }
        

        ### RESPONSES
        
        # Edit Benefit Data
        # BODY: 
        {
            "status": "success",
            "message": "Benefit updated successfully",
            "data": {
                "id_benefit": 1,
                "name": "Gebyar Diskon",
                "description": "Spesial 11/11",
                "point_required": 150,
                "discount": 20
            }
        }
        # STATUS CODE:
        # OK | 200
        
        # Edit Benefit Data (Benefit Not Found)
        # BODY: 
        {
            "status": "error",
            "message": "Benefit not found"
        }
        # STATUS CODE:
        # Not Found | 404
        
        pass

