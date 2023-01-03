from flask import Flask, send_file
import re

app = Flask('app')

name = open("name.txt").read()
config = []

def update_config():
  global config
  try:
    file = open("config.txt", "r")
    data = file.readlines()
    file.close()
    del file
    count = 0
    while count < len(data):
      data[count] = re.sub("\n||USERNAME: ||PASSWORD: ||FILE_SHARE: ", "", data[count])
      count += 1
    if data[2] == "allowed":
      data[2] = True
    else:
      data[2] = False
    config = data
  except:
    config = ['user', '1234', True]

@app.route('/')
def home():
  update_config()
  global name
  name = open("name.txt").read()
  return name

@app.route('/sent')
def sent():
  update_config()
  return send_file(str(name), as_attachment=True)

@app.route('/request/<username>/<password>/<file>')
def request(username, password, file):
  update_config()
  print(password)
  if username == config[0] and password == config[1] and config[2] == True:
    return send_file(file, as_attachment=True)
  else:
     return "INCORRECT"

app.run(host='0.0.0.0', port=8080)