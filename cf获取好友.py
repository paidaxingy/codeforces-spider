import requests
from lxml import etree
def get_proxy():
    return requests.get("http://demo.spiderpy.cn/get/").json().get('proxy')
# 基本信息
handleOrEmail=input('输入你的cf账号:')
password=input('输入你的密码:')
url='https://codeforces.com/enter?back=%2Ffriends'
proxies={'http':f'http://{get_proxy()}'}
data={
'csrf_token': 'fddf340cb0116b1d821244a6553ee362',
'action': 'enter',
'ftaa': 'kiw2y29as3yyqj772t',
'bfaa': '17c90512b38ed25c032584c16ffc3647',
'handleOrEmail': handleOrEmail,
'password': password,
'_tta': '661'
}
session=requests.session()
r=session.post(url,data=data)
r.encoding='UTF-8'
if r.text.find('Invalid')!=-1:
    print('账号或密码输入错误')
else:
    html=etree.HTML(r.content)
    result=html.xpath('//td[@style="text-align:left;"]/a/text()')
    print('你的好友列表')
    for name in result:
        if name != 'Countries' and name != 'Cities' and name != 'Organizations':
            print(name)
input('输入回车退出')
