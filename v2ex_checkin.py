# -*- coding: utf-8 -*-
import requests
import time

# 获取V2EX的登录页面
login_url = 'https://www.v2ex.com/signin'
login_page = requests.get(login_url).text

# 从登录页面中提取出csrf token
csrf_token = login_page.split('name="once" value="')[1].split('"')[0]

# 构造登录请求的数据
login_data = {
    'username': 'shyrock@163.com',
    'password': 'gogJpMFnCGRjuKMMJ?MJ',
    'once': csrf_token,
}

# 发送登录请求
login_response = requests.post(login_url, data=login_data)

# 如果登录成功，则获取V2EX的签到页面
if login_response.status_code == 200:
    checkin_url = 'https://www.v2ex.com/mission/daily'
    checkin_page = requests.get(checkin_url).text

    # 从签到页面中提取出csrf token
    csrf_token = checkin_page.split('name="once" value="')[1].split('"')[0]

    # 构造签到请求的数据
    checkin_data = {
        'once': csrf_token,
    }

    # 发送签到请求
    checkin_response = requests.post(checkin_url, data=checkin_data)

    # 如果签到成功，则打印签到成功的信息
    if checkin_response.status_code == 200:
        print('签到成功！')
    else:
        print('签到失败！')
else:
    print('登录失败！')
