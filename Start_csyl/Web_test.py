import pytest
import requests
def web_login():
    url='https://cvstest01.info-plus.cn/KIT/homePage/doLogin'
    data={
     "userName":"13839990000",
    "password":"4297F44B13955235245B2497399D7A93"
    }
    req=requests.post(url=url,data=data)
    print(req.status_code)
    print(req.text)

if __name__ == '__main__':
    web_login()