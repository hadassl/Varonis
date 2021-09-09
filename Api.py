import jwt
from cryptography.hazmat.primitives import serialization

from flask import Flask, render_template
import jinja2


app = Flask(__name__, template_folder='/templates')
#app.config['KEY'] = 'test'


# define Payload data
payload_data = {
  "username": "hadas",
  "password": "test"
}
key = "test"

# Test - get token_key based on payload data and the keygen configuration
private_key = open('keygen_config','r').read()
token_key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

@app.route('/token')
def tokens():
  try:
    # The algorithm was found using the line - jwt.get_unverified_header(token)
    token = jwt.encode(payload=payload_data, key=key, algorithm='HS256')
    #data = jwt.decode(token, app.config['KEY'])
    #print(data)
  except:
    print("a")


@app.route('/data/', methods=['POST'])
def data():
    return render_template('user_form.html')


if __name__ == "__main__":
  app.run(host="localhost", port=5000)