"""
后台管理--登录接口测试用例
"""
import requests
def test_login():
    url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
    data={
        "userName":"13839990000",
        "password":"4297F44B13955235245B2497399D7A93"
    }
    req=requests.post(url=url,data=data)
    print(req.text)

if __name__ == '__main__':
    test_login()