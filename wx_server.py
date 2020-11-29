from flask import Flask, request, render_template
import json

import get_info
import database

app = Flask(__name__)

db = database.DataBase()

@app.route('/')
def index():
    return "hello world"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        print(str(data, encoding='utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        username = json_data.get("username")
        password = json_data.get("password")
        user_info = get_info.getInfo(username, password)
        
        #db.login_process(user_info);
        #return json.dumps(lesson_dict)
        return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000, ssl_context=('ning.crt', 'ning.key'))
    #app.run(debug=True, host='0.0.0.0', port=8000)
