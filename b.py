#路由器路由模式下使用的
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
#driver = webdriver.Firefox()   # Firefox浏览器
# driver = webdriver.Firefox("驱动路径")
#driver = webdriver.Chrome()    # Chrome浏览器
from selenium.webdriver.support.select import Select
from time import sleep
import uuid
import socket
#https://github.com/Tecbin/PythonNet/
print('https://github.com/Tecbin/PythonNet/')
print('===================================')
# 查看当前主机名
print('当前主机名称为 : ' + socket.gethostname())
# 根据主机名称获取当前IP
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))
# Mac下上述方法均返回127.0.0.1
# 通过使用socket中的getaddrinfo中的函数获取真真的IP
# 下方代码为获取当前主机IPV4 和IPV6的所有IP地址
addrs = socket.getaddrinfo(socket.gethostname(),None)
for item in addrs:
    print(item)
# 仅获取当前IPV4地址
print('当前主机IPV4地址为:' + [item[4][0] for item in addrs if ':' not in item[4][0]][0])
# 同上仅获取当前IPV4地址
for item in addrs:
    if ':' not in item[4][0]:
        print('当前主机IPV4地址为:' + item[4][0])
        break
#find_element_by_id()
#find_element_by_name()
#find_element_by_class_name()
#find_element_by_tag_name()
#find_element_by_link_text()
#find_element_by_partial_link_text()
#find_element_by_xpath()
#find_element_by_css_selector()

txt, i = {}, 1

with open('1.txt', 'r', encoding='utf-8') as f:
    for ann in f.readlines():
        ann = ann.strip('\n')       #去除文本中的换行符
        print(ann)
        txt[i] = ann
        i += 1

#test_content = text_read('1.txt')  ip&mac

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

print(get_mac_address())
print(txt[1])
ip = socket.gethostbyname(socket.gethostname())
mac = get_mac_address()
print("-------------------")
print(mac)
print(ip)
#txt[4]

driver.get("http://10.2.5.251/a79.htm?wlanuserip=" + txt[4] +"&wlanacname=BRAS&url=http://1.1.1.1/&mac=" + mac) # 打开url网页 
driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[3]/div[2]/form/input[2]').send_keys(txt[1]) # 点击登入界面
driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[3]/div[2]/form/input[3]').send_keys(txt[2]) # 点击登入界面
sel = driver.find_element(By.NAME, "ISP_select")
Select(sel).select_by_index(txt[3])  # 显示50条
driver.find_element(By.XPATH, '//*[@id="edit_body"]/div[3]/div[2]/form/input[1]').click()
driver.implicitly_wait(10)
#browser.find_element_by_id('j-password').send_keys(Keys.ENTER)


#要打包成一个文件

#pyinstaller -F belle.py
