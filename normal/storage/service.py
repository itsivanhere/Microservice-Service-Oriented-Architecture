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

from rpc import StudentService

class RESTGatewayService(object):

    name = 'rest_gateway_service'

    user_rpc = RpcProxy('user_service')
    note_rpc = RpcProxy('note_service')

    session_provider = SessionProvider()
        
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
