#import packages
import json
from urllib import response, request, error

from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from entryPoint import http
from exception import UserNotFound, NoteNotFound
from provider.sessionProvider import SessionProvider

import cgi, os
import os
import cgitb; cgitb.enable()

import uuid
import urllib
from elasticsearch import Elasticsearch
import elasticsearch

from rpc import StudentService

class RESTGatewayService(object):

    name = 'rest_gateway_service'

    user_rpc = RpcProxy('user_service')
    note_rpc = RpcProxy('note_service')

    session_provider = SessionProvider()

    es=Elasticsearch(hosts="http://localhost:9200/")
    es=Elasticsearch()

    # For Testing Purpose

    @http("GET", "/api/users")
    def get_all_available_user(self, request):
        users = self.user_rpc.get_all_available_user()
        return Response(
            json.dumps(users),
            mimetype='application/json'
        )

    # Request login
    @http("POST", "/api/login")
    def login_user(self, request):
        data = request.json
        login_status = self.user_rpc.get_id(
            data['email'], data['password'])
        # data_email=data['email']
        # data_password=data['password']
        # id_user=self.user_rpc.get_id(data_email,data_password)
        # result = {
        #     'status': 1,
        #     'msg': ''
        # }
        # if login_status != 0:
        #     session_id = self.session_provider.set_session(
        #         login_status['data'])
        #     result['msg'] = 'Success'
        # else:
        #     result['status'] = 0
        #     result['msg'] = 'Wrong Username or Password'

        # response = Response(
        #     json.dumps(result),
        #     mimetype='application/json'
        # )

        # if login_status['status'] == 1:
        #     response = Response(login_status['data'])
        #     response.set_cookie('session_id', session_id)
        if login_status and len(login_status)>0:
            login_status=login_status[0]
            session_id=self.session_provider.set_session(login_status)
            login_status['session_id']=session_id
            response=Response(str(login_status))
            response.set_cookie('SESSID', session_id)
            return response
        else:
            response=Response("login failed!")
            return response

    #Request logout
    @http('GET', '/logout')
    def logout(self, request):
        cookies = request.cookies

        if cookies:
            session_data = self.session_provider.delete_session(cookies['SESSID'])
            response = Response('Logout Succeed!')
            return response
        else:
            response = Response('Logout Failed!')
            return response

    #Request register
    @http('POST', '/api/register')
    def register_data(self, request):
        data_nrp = request.get_json()['nrp']
        data_nama=request.get_json()['nama']
        data_email=request.get_json()['email']
        data_password=request.get_json()['password']
        entry=self.user_rpc.register_data(data_nrp,data_nama,data_email,data_password)
        return u"Received: {}".format(request.get_data(as_text=True))

    # Request Body

    # {
    # "nrp": "C14190191",
    # "nama": "Chris",
    # "email": "c14190191@john.petra.ac.id",
    # "password": "hai789"
    # }

    #Request upload file
    @http('POST', '/upload')
    # def upload_paper(self,request):
    #     form = cgi.FieldStorage()
    # # Get filename here.
    #     fileitem = request.form.get('filename')
    # # Test if the file was uploaded
    #     if fileitem.filename:
    #         fn = os.path.basename(fileitem.filename)
    #         open('/tmp/' + fn, 'wb').write(fileitem.file.read())
    #         message = 'The file "' + fn + '" was uploaded successfully'
    #     else:
    #         message = 'No file was uploaded'
    #     return 
        # fi = form['filename']
        # if fi.filename:
	    #     fil = os.path.basename(fi.filename)
	    #     # open for reading & writing the file into the server
	    #     open(fn, 'wb').write(fi.file.read())
        
    def upload_file(self, request):
        #print("request data")
        cookies = request.cookies
        session_data=None
        if cookies:
            print("Cek student: "+cookies["SESSID"])
            session_data = self.session_provider.get_session(str(cookies['SESSID']))

        if (session_data!=None):
            for file in request.files.items():
                _, file_storage = file
                lowercase_str = uuid.uuid4().hex
                #print("File "+file_storage.filename)
                fnameakhir=lowercase_str+file_storage.filename
                fname="upload/"+fnameakhir
                self.user_rpc.add_file(session_data['id'],fname)

                file_storage.save(f"{fname}")
            return json.dumps({"Cek": True})
        else :
            return "failed"

    #Request download file
    @http('GET', '/download')
    def download_paper(self,request):
        filedata = urllib.request.urlopen('tiket.com.pdf')
        datatowrite = filedata.read()
        with open('/Users/SOA', 'wb') as f:
            f.write(datatowrite)

        # testfile = urllib.URLopener()
        # testfile.retrieve("http://randomsite.com/file.gz", "file.gz")

    #search with elasticsearch
    @http('GET', '/search/title')
    def search_file(self,request,title):
        result=Elasticsearch().index(index=title, doc_type="sentence", id=1)
        response=Response(result)
        return response
