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
    cookies={"SESSION":"ZThhZWUyZmEtNjU3Ni00OTUzLWI3ZTUtZGY3MGE5NmQyYmVl"}
    req=requests.post(url=url,json=json,cookies=cookies)
    print(req.text)
if __name__ == '__main__':
    test_01_ProductQuery()