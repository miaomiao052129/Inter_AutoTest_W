"""
后台管理--登录接口测试用例
"""
from utils.RequestUtils import requests_ht_login
import requests
def test_login():
    url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
    data={
        "userName":"13839990000", #用户名
        "password":"4297F44B13955235245B2497399D7A93" #密码
    }
    r=requests_ht_login(url,data) #调用封装的RequestsUtils.py文件中的封装的方法名
    print(r)

if __name__ == '__main__':
    test_login()