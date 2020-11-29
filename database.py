import pymysql

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
    def login_process(self, user_info):
        #print(user_info)
        groups = self.query_user_group(user_info['username']) # try to query user group
        if len(groups) > 0:
            return groups
        else:
            self.insert_user(user_info['username'], user_info['academy'], user_info['type'], user_info['name'])
            for group in user_info['groups']:
                self.insert_group_info(group['groupID'], group['groupName'], group['type'])
                self.insert_group_user(group['groupID'], user_info['username'])
    
        groups = self.query_user_group(user_info['username']) # try to query user group
    
        #self.query_user(user_info['username'])
    def query_group_notice(self, gno):
        values = ['noticeID', 'noticeContent', 'noticeTime']
        sql = "SELECT nno, ncontent, ntime FROM noticeinfo WHERE gno = '%s'" % (gno)
        self.cursor.execute(sql)
        notices = self.cursor.fetchall()
        notices = list(notices)
        print(type(notices[0][2]))

        #print(result)
        new_notices = [dict(zip(values, notice)) for notice in notices]
        return new_notices


    def query_user_group(self, uno):
        values = ['groupID', 'groupName', 'type']
        sql = "SELECT groupinfo.gno, gname, gtype FROM groupinfo, groupuser\
                WHERE groupinfo.gno = groupuser.gno AND groupuser.uno = '%s'" % (uno)
        self.cursor.execute(sql)
        groups = self.cursor.fetchall()
        groups = list(groups)

        #print(result)
        new_groups = [dict(zip(values, group)) for group in groups]
        return new_groups

    def insert_user(self, uno, uacademy, utype, uname):
        sql = "INSERT INTO user(uno, uacademy, utype, uname)\
            VALUES ('%s', '%s', '%s', '%s')" % (uno, uacademy, utype, uname)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()# 发生错误时回滚

    def insert_group_info(self, gno, gname, gtype):
        sql = "INSERT INTO groupinfo(gno, gname, gtype)\
            VALUES ('%s', '%s', '%s')" % (gno, gname, gtype)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def insert_group_user(self, gno, uno):
        sql = "INSERT INTO groupuser(gno, uno)\
            VALUES ('%s', '%s')" % (gno, uno)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def query_user(self, uno):
        sql = "SELECT * FROM user WHERE uno = '%s'" % (uno)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(type(result[0]))
        print(result[0])

