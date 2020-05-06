from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup


class lesson:
    class_id = ""
    class_name = ""

def getInfo(username, password):
    if password == "admin":
        return {"name": username, "type": "admin", "username": username}

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome()
    browser.get("http://us.nwpu.edu.cn/eams/login.action")
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    switch = browser.find_element_by_id("local_zh").click()
    submit = browser.find_element_by_class_name("submit_button").click()
    print("login")
    browser.refresh()
    sleep(1)
    print("refreshed")
    f = open("table.html", 'w')
    f.write(browser.page_source)
    f.close()
    bs = BeautifulSoup(browser.page_source, 'html.parser')
    tables = bs.find('tbody', {'id': "grid12042826911_data"})
    lessons = []
    data_key = []
    data_value = []

    name = bs.find('p', {"class": "person_title_1"}).get_text()
    academy = bs.find('p', {"class": "person_title_2"}).get_text()
    classes = []
    for table in tables:
        class_id = table.a.get_text()
        class_name = table.td.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        class_dict = {"groupID":class_id, "groupName":class_name,  "type": "class"}
        classes.append(class_dict)
        #for l in lessons:
            #print(l.class_id, l.class_name)
    
    data_dict = {"name":name, "academy":academy, "groups":classes, "username":username, "type": "student"}
    return data_dict


if __name__ == "__main__":
    getClass("2018300410", "q1w2e3r4314159")

