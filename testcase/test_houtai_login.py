import pytest
import requests
class Test_Login:
    # 登录
    def test_login(self):
        url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
        data={
            "userName":"13839990000",
            "password":"4297F44B13955235245B2497399D7A93"
        }
        req=requests.post(url=url,data=data)
        print(req.text)
        print(req.status_code)
if __name__ == '__main__':
    pytest.main(['-v','-s','test_houtai_login.py'])