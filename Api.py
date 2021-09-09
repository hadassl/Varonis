import jwt
from cryptography.hazmat.primitives import serialization

import json

from sanic import Sanic
from sanic.response import s_json
from sanic.jwt import initizlize, exceptions

from Users import User, usernames, uids


def auth(request):
    """
    This function get the request, pull the username & password and compare it to the Users data
    :param request: http request
    :return: user
    """
    username = request.json.get("username")
    password = request.json.get("password")
    # check if the parameters are valid
    if not username or not password:
        print("There is missing parameter in Auth data")
        raise exceptions.AuthenticationFailed("There is missing parameter in Auth data")
    else:
        user = usernames.get(username)
        if user is None:
            print("The user was not found")
            raise exceptions.AuthenticationFailed("The user was not found")"
        if password != user.password:
            print("The password is in-correct")
            raise exceptions.AuthenticationFailed("The password is in-correct")
        return user

# define the app
app = Sanic()
initialize(app, authenticate=auth)


@app.post('/test')
async def inUsers(request):
    return s_json(request.json)


if __name__ == "__main__":
  app.run(host="localhost")

# define Payload data
#payload_data = {
#  "username": "hadas",
#  "password": "test"
#}
#key = "test"

# Test - get token_key based on payload data and the keygen configuration
#private_key = open('keygen_config','r').read()
#token_key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

#@app.route('/token')
#def tokens():
#  try:
#    # The algorithm was found using the line - jwt.get_unverified_header(token)
#    token = jwt.encode(payload=payload_data, key=key, algorithm='HS256')
#    #data = jwt.decode(token, app.config['KEY'])
#    #print(data)
#  except:
#    print("a")


