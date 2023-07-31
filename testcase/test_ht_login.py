
from utils.RequestUtils import requests_ht_login,requests_ht_ProductQuery,requests_ht_xptjgl_xz
# import requests
# def test_ht_login():
#     """
#     后台登录
#     :return:
#     """
#     url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
#     data={
#         "userName":"13839990000", #用户名
#         "password":"4297F44B13955235245B2497399D7A93" #密码
#     }
#     r=requests_ht_login(url,data) #调用封装的RequestsUtils.py文件中的封装的方法名
#     print(r)
# def test_ht_ProductQuery():
#     """
#     商品图片管理页面-查询功能
#     :return:
#     """
#     url = 'https://cvstest01.info-plus.cn/aplus_mgr//H0001'
#     json = {
#         "cateId": "10",
#         "order": "",
#         "itemImg": "",
#         "itemCd": "",
#         "itemSale": "",
#         "itemOrder": "",
#         "pageSize": 10,
#         "curIndex": 1,
#         "screenName": ""
#     }
#     cookies = {"SESSION": "NjkwODE3ZjAtNTI4NS00ODQxLWJiOTQtMWRlY2RhZGEyMTMx"}  #session会过期,需要登录再次获取一下session
#     r=requests_ht_ProductQuery(url=url,json=json,cookies=cookies)
#     print(r)
#
# def test_ht_xptjgl_xz():
#     """
#     新品推荐管理-新增
#     :return:
#     """
#     url='https://cvstest01.info-plus.cn/aplus_mgr/H0004/SavaItem'
#     params={
#         'itemId': '3326739',
#         'itemName': '%E3%80%90%E6%B1%B0%E3%80%91%E4%B8%AD%E5%9B%BD%E5%8A%B2%E9%85%92520ml',
#         'orderPrice': '38.75',
#         'itembars': '6909131280647', #商品条码
#         'grossMargin': '',
#         'salePrice': '65',
#         'warrantyDays': '0.0',
#         'recommandInfo': '%E6%8E%A8%E8%8D%90%E7%90%86%E7%94%B1',
#         'exhibitInfo': '%E9%99%88%E5%88%97%E5%BB%BA%E8%AE%AE',
#         'beginDate': '2023-07-08',
#         'endDate': '2023-07-09',
#         'replaceItem': '',
#         'template': '1',
#         'imgUrl1': '',
#         'imgUrl2':''
#     }
#     cookies={"SESSION":"NjkwODE3ZjAtNTI4NS00ODQxLWJiOTQtMWRlY2RhZGEyMTMx"}
#     res=requests_ht_xptjgl_xz(url=url,params=params,cookies=cookies)
#     print(res)


def test_ht_login():
    """
    后台登录
    :return:
    """
    url='https://cvstest01.info-plus.cn/aplus_mgr/homePage/doLogin'
    data={
        "userName":"13839990000", #用户名
        "password":"4297F44B13955235245B2497399D7A93" #密码
    }
    from utils.RequestUtils import Requests_HouTai #导入这个类
    request=Requests_HouTai()   #对这个类初始化一下，初始化一个类
    r=request.get_houtai(url,data=data)
    print(r)
def test_ht_ProductQuery():
    """
    商品图片管理页面-查询功能
    :return:
    """
    url = 'https://cvstest01.info-plus.cn/aplus_mgr//H0001'
    json = {
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
    cookies = {"SESSION": "NjkwODE3ZjAtNTI4NS00ODQxLWJiOTQtMWRlY2RhZGEyMTMx"}  #session会过期,需要登录再次获取一下session
    from utils.RequestUtils import Requests_HouTai
    request=Requests_HouTai()
    r=request.post_houtai(url=url,json=json,cookies=cookies)
    print(r)
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
    cookies={"SESSION":"NjkwODE3ZjAtNTI4NS00ODQxLWJiOTQtMWRlY2RhZGEyMTMx"}
    from utils.RequestUtils import Requests_HouTai
    request=Requests_HouTai()
    r=request.get(url=url,params=params,cookies=cookies)
    print(r)
