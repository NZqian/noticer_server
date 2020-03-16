from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup


class lesson:
    class_id = ""
    class_name = ""

def getClass(username, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome()
    browser.get("http://us.nwpu.edu.cn/eams/login.action")
    browser.find_element_by_id("username").send_keys("2018300410")
    browser.find_element_by_id("password").send_keys("q1w2e3r4314159")
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
    data_key.append("name")
    data_key.append("academy")
    data_value.append(name)
    data_value.append(academy)
    for table in tables:
        cur_lesson = lesson()
        cur_lesson.class_id = table.a.get_text()
        cur_lesson.class_name = table.td.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        data_key.append(cur_lesson.class_id)
        data_value.append(cur_lesson.class_name)
        lessons.append(cur_lesson)
        #for l in lessons:
            #print(l.class_id, l.class_name)
    lesson_dict = dict(zip(data_key, data_value))
    return lesson_dict


if __name__ == "__main__":
    getClass("2018300410", "q1w2e3r4314159")

