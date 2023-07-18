import requests
#1、创建一个封装的GET方法
#2、发送requests get请求
#3、获取结果响应内容
#4、内容存到字典
#5、返回字典
def requests_ht_login(url,data):
    """
     【后台管理-登录】
    :param url: 后台登录地址
    :param data: 后台登录参数
    :return: 返回值
    """
    req=requests.post(url=url,data=data)
    code=req.status_code
    try:
        body=req.json()
    except Exception as e:
        body=req.text
    dic=dict()
    dic["code"]=code
    dic["body"]=body
    return dic
def requests_ht_ProductQuery(url,json,cookies):
    """
    【后台管理-商品图片管理页面-查询功能】
    :param url: 商品url
    :param json: 参数
    :param cookies:
    :return: dict
    """
    reqProductQuery=requests.post(url=url,json=json,cookies=cookies)
    code=reqProductQuery.status_code
    try:
        body = reqProductQuery.text
    except Exception as e:
        body = reqProductQuery.json()
    dic=dict()
    dic['code']=code
    dic['body']=body
    return dic

def requests_ht_xptjgl_xz(url,params,cookies):
    """
    【后台管理-新品推荐管理-新增】
    :param url: 新品推荐管理新增接口地址
    :param params: 参数
    :param cookies:
    :return:
    """
    reqxptjglxz=requests.get(url=url,params=params,cookies=cookies)
    code=reqxptjglxz.status_code
    try:
        body = reqxptjglxz.text
    except Exception as e:
        body=reqxptjglxz.json()
    dic=dict()
    dic['code']=code
    dic['body']=body
    return dic