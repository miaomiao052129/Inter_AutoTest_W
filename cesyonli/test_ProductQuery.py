"""
后台管理-商品图片管理页面-查询功能
"""
import pytest
import requests
def test_01_ProductQuery():
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

    print(req.status_code)
if __name__ == '__main__':
    test_01_ProductQuery()