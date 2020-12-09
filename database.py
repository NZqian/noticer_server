import pymysql
import get_info

'''
conn = pymysql.connect(
    host="139.9.119.34",
    user="s2018300410",
    password="GaussDB@123",
    database="noticer")

print(conn)
print(type(conn))
'''


class DataBase:

    def __init__(self, host="139.9.119.34", user="s2018300410", password="GaussDB@123", database="noticer"):
        self.conn = pymysql.connect(host, user, password, database)
        self.cursor = self.conn.cursor()

    # if user not exist, insert data into relative tables
    # return groups info of the user
    def login_process(self, username, password):
        #print(user_info)
        res = self.query_user(username, password)
        groups = []
        user_info = {}
        print(res)
        if res == 2:
            user_info = get_info.getInfo(username, password)
            self.insert_user(user_info['username'], user_info['academy'], user_info['type'], user_info['name'], password)
            if user_info['type'] != "admin":
                for group in user_info['groups']:
                    self.insert_group_info(group['groupID'], group['groupName'], group['type'])
                    self.insert_group_user(group['groupID'], user_info['username'])
        elif res == -1:
            return "error"
        #if user_info['type'] != "admin":
        #else groups 
        groups = self.query_user_group(username) # try to query user group
        userinfo = self.query_user_info(username)
        return {"userinfo": userinfo, "groups": groups}

    def update_notice_recieve(self, nno, uno):
        print(nno, uno)
        sql = "update noticeuser set received = 1 \
                where nno = '%s' and uno='%s'" % (nno, uno)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()# 发生错误时回滚

    def query_notice_detail_user(self, nno, uno):
        values = ['title', 'content', 'time', 'received']
        sql = "select ntitle, ncontent, ntime, received from noticeuser, noticeinfo where \
                noticeuser.uno='%s' and noticeuser.nno=noticeinfo.nno and noticeuser.nno=%s;"\
                % (uno, nno)
        self.cursor.execute(sql)
        notice = self.cursor.fetchall()[0]
        notice = dict(zip(values, notice))
        notice['date'] = notice['time'].strftime('%Y-%m-%d')
        notice['time'] = notice['time'].strftime('%H-%M-%S')
        notice['notice_no'] = nno
        return notice
    
    def query_user_info(self, username):
        values = ['username', 'academy', 'type', 'name']
        sql = "SELECT uno, uacademy, utype, uname FROM user\
                WHERE uno = '%s'" % (username)
        self.cursor.execute(sql)
        userinfo = list(self.cursor.fetchall())[0]
        return dict(zip(values, userinfo))


        #self.query_user(user_info['username'])
    def query_group_notice(self, gno):
        values = ['noticeID', 'noticeTitle']
        sql = "SELECT nno, ntitle FROM noticeinfo WHERE gno = '%s'" % (gno)
        self.cursor.execute(sql)
        notices = self.cursor.fetchall()
        notices = list(notices)

        #print(result)
        new_notices = [dict(zip(values, notice)) for notice in notices]
        return new_notices

    def query_all_group(self):
        values = ['groupID', 'groupName', 'groupType']
        sql = "SELECT groupinfo.gno, gname, gtype FROM groupinfo"
        self.cursor.execute(sql)
        groups = self.cursor.fetchall()
        groups = list(groups)

        #print(result)
        new_groups = [dict(zip(values, group)) for group in groups]
        return new_groups


    def query_user_group(self, uno):
        values = ['groupID', 'groupName', 'groupType']
        sql = "SELECT groupinfo.gno, gname, gtype FROM groupinfo, groupuser\
                WHERE groupinfo.gno = groupuser.gno AND groupuser.uno = '%s'" % (uno)
        self.cursor.execute(sql)
        groups = self.cursor.fetchall()
        groups = list(groups)

        #print(result)
        new_groups = [dict(zip(values, group)) for group in groups]
        return new_groups

    def insert_user(self, uno, uacademy, utype, uname, password):
        print(uno, uacademy, utype, uname, password)
        sql = "INSERT INTO user(uno, uacademy, utype, uname, password)\
            VALUES ('%s', '%s', '%s', '%s', '%s')" % (uno, uacademy, utype, uname, password)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("insert user success")
        except:
            self.conn.rollback()# 发生错误时回滚
            print("insert user fail")

    def insert_group_info(self, gno, gname, gtype):
        sql = "INSERT INTO groupinfo(gno, gname, gtype)\
            VALUES ('%s', '%s', '%s')" % (gno, gname, gtype)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def insert_group_user(self, gno, uno):
        print(gno, uno)
        sql = "INSERT INTO groupuser(gno, uno)\
            VALUES ('%s', '%s')" % (gno, uno)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("success")
        except:
            self.conn.rollback()
            print("fail")

    def query_user(self, uno, password):
        sql = "SELECT * FROM user WHERE uno = '%s'" % (uno)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result) > 0:
            sql = "SELECT * FROM user WHERE uno = '%s' \
                    AND password = '%s'" % (uno, password)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) > 0:
                return 1
            else:
                return -1
        else:
            return 2


