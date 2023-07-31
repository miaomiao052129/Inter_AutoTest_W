import pytest
import requests
def web_login():
    """
    A+WEB：登录接口
    :return:
    """
    url='https://cvstest01.info-plus.cn/KIT/homePage/doLogin'
    data={
     "userName":"13839990000",
    "password":"4297F44B13955235245B2497399D7A93"
    }
    req=requests.post(url=url,data=data)
    print(req.status_code)
    print(req.text)
def T2001Ajax(params=None):
    """
    A+WEB：分类月别构成分析（旧）
    :return:
    """
    url='https://cvstest01.info-plus.cn/KIT/T2001/T2001Ajax?'
    params={
        "select":" 0",
        "date":"",
        "order":"",
        "categoryId":"",
        "categoryLevel":"1",
        "storegroup_code":"",
        "storeId:164":""
    }
    Cookie={"SESSION":"MDFlMzJhNGItMzhiZi00ODAwLWEzODktNTY5YTliMjJlYTQ1"}
    req=requests.get(url=url,params=params,cookies=Cookie)
    print(req.status_code)
    print(req.json())
if __name__ == '__main__':
    web_login()
    T2001Ajax()
