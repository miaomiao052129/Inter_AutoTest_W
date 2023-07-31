
import requests
def test_login():
    """
    后台管理--登录接口测试用例
    :return:
    """
    url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
    data={
        "userName":"13839990000", #用户名
        "password":"4297F44B13955235245B2497399D7A93" #密码
    }
    req=requests.post(url=url,data=data)
    print(req.status_code)

def test_01_ProductQuery():
    """
    后台管理-商品图片管理页面-查询功能
    :return:
    """
    url='https://cvstest01.info-plus.cn/aplus_mgr//H0001'
    json={
        "cateId": "10",
        "order": "",
        "itemImg": "",
        "itemCd": "",
        "itemSale": "",
        "itemOrder": "",
        "pageSize": 10,
        "curIndex": 1,
        "screenName": ""
    }
    cookies={"SESSION":"YWJkMGIzNzctNzljMC00ZDE2LTgwMzEtZGQ5NThmZmIyOTVj"} #session会过期

    req=requests.post(url=url,json=json,cookies=cookies)
    print(req.text)

def test_xptjgl_xz():
    """
    新品推荐管理-新增
    :return:
    """
    url='https://cvstest01.info-plus.cn/aplus_mgr/H0004/SavaItem'
    params={

        'itemId': '3326739',
        'itemName': '%E3%80%90%E6%B1%B0%E3%80%91%E4%B8%AD%E5%9B%BD%E5%8A%B2%E9%85%92520ml',
        'orderPrice': '38.75',
        'itembars': '6909131280647',
        'grossMargin': '',
        'salePrice': '65',
        'warrantyDays': '0.0',
        'recommandInfo': '%E6%8E%A8%E8%8D%90%E7%90%86%E7%94%B1',
        'exhibitInfo': '%E9%99%88%E5%88%97%E5%BB%BA%E8%AE%AE',
        'beginDate': '2023-07-08',
        'endDate': '2023-07-09',
        'replaceItem': '',
        'template': '1',
        'imgUrl1': '',
        'imgUrl2':''
    }
    cookies={"SESSION":"NjkwODE3ZjAtNTI4NS00ODQxLWJiOTQtMWRlY2RhZGEyMTMx"}
    res=requests.get(url=url,params=params,cookies=cookies)
    print(res.text)
    print(res.status_code)
if __name__ == '__main__':
    test_login()