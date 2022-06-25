import pickle
import uuid

class SessionWrapper:
    
    def __init__(self, connection):
        # Redis Connection
        self.redis = connection

        # 1 Hour Expire (in Second)
        self.default_expire = 60 * 60
    
    def generate_session_id(self):
        key = str(uuid.uuid4())
        while self.redis.exist(key):
            key = str(uuid.uuid4())
        return key

    def set_session(self, user_data):
        # Pickle User Data so that can be stored in Redis
        user_data_pickled = pickle.dumps(user_data)

        # Get Session ID
        session_id = self.generate_session_id()

        # Store Session Data with Expire Time in Redis
        self.redis.set(session_id, user_data_pickled, ex=self.default_expire)

        return session_id
    
    def get_session(self, session_id):
        # Get the Data from Redis
        result = self.redis.get(session_id)

        # Unpack the user data from Redis
        user_data = pickle.loads(result)

        return user_data