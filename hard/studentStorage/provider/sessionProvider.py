import redis
from nameko.extensions import DependencyProvider

from wrapper.sessionWrapper import SessionWrapper

class SessionProvider(DependencyProvider):

    def setup(self):
        self.client = redis.Redis(host='localhost', port=16379, db=0)
    
    def get_dependency(self, worker_ctx):
        return SessionWrapper(self.client)
