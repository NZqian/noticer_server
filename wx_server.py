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
        #user_info = get_info.getInfo(username, password)
        userinfo = db.login_process(username, password)
        
        #db.login_process(user_info);
        #return json.dumps(lesson_dict)
        print(userinfo)
        return json.dumps(userinfo)

@app.route('/add_admin_into_group/', methods=['GET', 'POST'])
def add_admin_into_group():
    if request.method == 'POST':
        data = request.get_data()
        print(str(data, encoding='utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        group_no = json_data.get("group_no")
        user_no = json_data.get("user_no")
        db.insert_group_user(group_no, user_no)
        return "OK"

@app.route('/notice_receive/', methods=['GET', 'POST'])
def notice_recieve():
    if request.method == 'POST':
        data = request.get_data()
        print(str(data, encoding='utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        notice_no = json_data.get("notice_no")
        user_no = json_data.get("user_no")
        db.update_notice_recieve(notice_no, user_no)
        return "OK"

@app.route('/notice_single_user/', methods=['GET', 'POST'])
def notice_detail_user():
    if request.method == 'POST':
        data = request.get_data()
        print(str(data, encoding='utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        notice_no = json_data.get("notice_no")
        user_no = json_data.get("user_no")
        notice = db.query_notice_detail_user(notice_no, user_no)
        
        print(notice)
        return json.dumps(notice)

@app.route('/noticeinfo/', methods=['GET', 'POST'])
def notice_info():
    if request.method == 'POST':
        data = request.get_data()
        print(str(data, encoding='utf-8'))
        json_data = json.loads(data.decode('utf-8'))
        groupID = json_data.get("groupID")
        notices = db.query_group_notice(groupID)
        
        print(notices)
        return json.dumps(notices)

@app.route('/get_all_group/', methods=['GET', 'POST'])
def get_all_group():
    if request.method == 'GET':
        groups = db.query_all_group()
        print(groups)
        
        return json.dumps(groups)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000, ssl_context=('ning.crt', 'ning.key'))
    #app.run(debug=True, host='0.0.0.0', port=8000)
