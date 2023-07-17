"""
新品推荐管理-新增
"""
import pytest
import requests
def test_xptjgl_xz():
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
    cookies={"SESSION":"ZThhZWUyZmEtNjU3Ni00OTUzLWI3ZTUtZGY3MGE5NmQyYmVl"}
    res=requests.get(url=url,params=params,cookies=cookies)
    print(res.text)
    print(res.status_code)