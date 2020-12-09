import json
import get_info
import database

db = database.DataBase()

'''
username = "2018300410"
password = "q1w2e3r4314159"
user_info = get_info.getInfo(username, password)
'''
user_info = {'groups': [{'groupID': 'U10M11011.04', 'groupName': '数据库原理', 'type': 'class'}, {'groupID': 'U10M11016.04', 'groupName': '计算机网络原理', 'type': 'class'}, {'groupID': 'U10M11026.01', 'groupName': '物联网导论', 'type': 'class'}, {'groupID': 'U10M11074.01', 'groupName': '软件测试', 'type': 'class'}, {'groupID': 'U10M11121.01', 'groupName': '人工智能', 'type': 'class'}, {'groupID': 'U10M11125.01', 'groupName': '生物大数据分析', 'type': 'class'}, {'groupID': 'U10M13008.02', 'groupName': '计算机操作系统（双语）', 'type': 'class'}, {'groupID': 'U10P31008.03', 'groupName': '计算机网络原理实验', 'type': 'class'}, {'groupID': 'U10P31010.03', 'groupName': '数据库原理实验', 'type': 'class'}, {'groupID': 'U10P33019.03', 'groupName': '计算机操作系统实验（双语）', 'type': 'class'}, {'groupID': 'U31G71041.01', 'groupName': '跆拳道中级', 'type': 'class'}, {'groupID': 'U42L11203.01', 'groupName': '中国青铜艺术鉴赏', 'type': 'class'}, {'groupID': 'academy', 'groupName': '计算机学院', 'type': 'academy'}], 'username': '2018300410', 'academy': '计算机学院', 'type': 'student', 'name': '宁子谦'}

username = "2018300410"
password = "q1w2e3r4314159"
#result = db.login_process(username, password)
#result = db.query_group_notice("U10M11011.04")
result = db.query_notice_sigle_user("1", "2018300410")
print(result)
