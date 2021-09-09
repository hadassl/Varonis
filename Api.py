import json

from sanic import Sanic
from sanic.response import s_json
from sanic.jwt import initizlize, exceptions

from Users import User, usernames, uids


def get_json_val(value):
    """
    This function get the data of the filed name in the json
    :param value: string value
    :return: the value itself
    """
    return [item for key, item in value.items()][0]


def normalization(request_data):
    """
    This function get the request json and return the name value
    :param request_data: json request data
    :return: json - name: name
    """
    return {value["name"]: get_json_val(value) for value in request_data}


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
    data = normalization(request.json)
    return s_json(data)


if __name__ == "__main__":
  app.run(host="localhost")




