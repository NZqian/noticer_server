from flask import Flask, request, render_template
import json

import get_class

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_data()
        json_data = json.loads(data.decode('utf-8'))
        username = json_data.get("username")
        password = json_data.get("password")
        #print(username, password)
        lesson_dict = get_class.getClass(username, password)
        print(lesson_dict)
        #print(len(lesson_dict))
        #return 'welcome, %s' % json_data.get("username")
        return json.dumps(lesson_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000, ssl_context=("./ning.crt", "./ning.key"))
