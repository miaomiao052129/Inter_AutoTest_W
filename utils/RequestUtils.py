import requests
#1、创建一个封装的GET方法
def requests_ht_login(url,data):
#2、发送requests get请求
    req=requests.post(url=url,data=data)
#3、获取结果响应内容
    code=req.status_code
    try:
        body=req.json()
    except Exception as e:
        body=req.text
#4、内容存到字典
    dic=dict()
    dic["code"]=code
    dic["body"]=body
#5、返回字典
    return dic

