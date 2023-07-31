import requests

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
    req=requests.post(url=url,json=json,cookies=cookies)
    code=req.status_code
    try:
        body = req.text
    except Exception as e:
        body = req.json()
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
    req=requests.get(url=url,params=params,cookies=cookies)
    code=req.status_code
    try:
        body = req.text
    except Exception as e:
        body=req.json()
    dic=dict()
    dic['code']=code
    dic['body']=body
    return dic

# 重构
#1、创建类（Requests_HouTai）
class Requests_HouTai:
# 2、定义公共方法（request_houtai）
    def request_houtai(self, url,params=None,json=None,cookies=None,data=None,method="get"):
        #（1）增加方法的参数，根据参数来验证方法get/post的方法请求
        if method=="get":
            req=requests.get(url=url,params=params,cookies=cookies)
            #执行get请求
        elif method=="post":
            #执行post请求
            req = requests.post(url=url, json=json, cookies=cookies,data=data)
        # （2）重复的内容复制进来
        code = req.status_code
        try:
            body = req.text
        except Exception as e:
            body = req.json()
        dic = dict()
        dic['code'] = code
        dic['body'] = body
        return dic
#3、重构get/post方法
    #（3.1) Get方法的重构
    #1、定义方法
    def get_houtai(self,url,**kwargs):
    #2、定义参数
        #url、json、cookies、cookies、data、method
    #3、调用公共方法
        return self.request_houtai(url,method="get",**kwargs)

#（3.1) Post方法的重构
    #1、定义方法
    def post_houtai(self,url,**kwargs):
    #2、定义参数
        #url、json、cookies、cookies、data、method
    #3、调用公共方法
        return self.request_houtai(url,method="post",**kwargs)