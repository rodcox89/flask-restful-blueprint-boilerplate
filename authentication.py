############################################################################################
# JWT Functions for Authenticating Users via API
############################################################################################

from db.models import user_datastore
from flask_security.utils import verify_password

# https://github.com/graup/flask-restless-security/blob/master/server.py
def authenticate(username, password):
    try:
        user = user_datastore.find_user(email=username)
    except KeyError:
        return None
    if username == user.email and verify_password(password, user.password):
        return user
    return None

def load_user(payload):
    user = user_datastore.find_user(id=payload['identity'])
    return user
