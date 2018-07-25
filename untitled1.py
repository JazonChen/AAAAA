# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:30:25 2018

@author: Administrator
"""
练习5：
1.优化代码，用函数的方式修改练习4 输出每一天的天气（函数）
2.打印温度折线图，使用函数来优化（必须有返回值）

import urllib.request as r
city=input('plz write down a city: ')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(city)).read().decode('utf-8','ignore')

import json
data=json.loads(data)

mul=len(data['list'])//8
list=[]
def opti():
    for i in range(0,mul+1):
            print('day'+str(i+1)+': ')
            print("situation: "+data['list'][2+i*8]['weather'][0]['description'])
            a=int(data['list'][2+i*8]['main']['temp'])
            list.append(a)
    return list
def pho():
    for j in range(0,len(list)):
        print(list[j]*'-')
opti()
pho()

练习6：
1.显示4个商品然后打印分割线，只要第一页36个商品信息
2.列出36个商品
3.获取所有的商品价格并且给商品排序，从高到低排序
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示。

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)

def goods():
    for i in range(0,36):
        print('ID:'+data['mods']['itemlist']['data']['auctions'][i]['user_id'])
        print('款式'+data['mods']['itemlist']['data']['auctions'][i]['title'])
        print('价格：'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        print('地址：'+data['mods']['itemlist']['data']['auctions'][i]['item_loc'])
        print('店名：'+data['mods']['itemlist']['data']['auctions'][i]['nick'])
        if i%4==0:print('='*60)

lis1=[]  
lis2=[]
def price():'''这段有错误'''
    for j in range(0,36):
           t=data['mods']['itemlist']['data']['auctions'][j]['title']
           p=float(data['mods']['itemlist']['data']['auctions'][j]['view_price'])           
           lis1.append(p)
           lis2.append(t)
           ##print(str(p)+t)
    a=sorted(lis2)
    a.reverse() #价格列表倒置
    mydict=dict(zip(a,lis1))#把数组导入字典
    print('商品价格从高到低：')
    for k in mydict.keys():#循环字典
        print('商品名：{}'.format(k))
        
lis3=[]
def sales():
    print('销量从高到低：')
    for g in range(0,36):
        x=data['mods']['itemlist']['data']['auctions'][g]['view_sales']
        d=float(x[0:-3])
        lis3.append(d)
    e=sorted(lis3)
    e.reverse()
    print(e)
 
def mail():
    for m in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][m]['view_fee'])==0.00:
            print('第{}件商品包邮'.format(m+1))
        else:
            print('第{}件商品不包邮'.format(m+1))
            break                      
goods()
price()
sales() 
mail()

练习7：
      1.使用多选其一，完成天气的提醒（if），淘宝客服端
      2.一定要多次使用for循环，偶尔使用while循环，在淘宝客户端
      3.使用到break或者continue
 1. 
def weather():
import urllib.request as r
city=input('plz write down a city: ')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(city)).read().decode('utf-8','ignore')

import json
data=json.loads(data)

for i in range(0,8):
    a=str(data['list'][i]['weather'][0]['main'])
    if a=='Rain':
        print('Gentle hint: rainly.')
    elif a=='Clouds':
        print('Gentle hint: cloudy.')
    elif a=='Clear':
        print('Gentle hint: sunny.')
weather()
2.
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)

def taobao():
    for i in range(0,36):
        print('第{}件商品：'.format(i+1))
        print('ID:'+data['mods']['itemlist']['data']['auctions'][i]['user_id'])
        print('款式'+data['mods']['itemlist']['data']['auctions'][i]['title'])
        print('')
        while (i+1)%6==0:
            print(str('=')*45)
            break
            
taobao()


    











