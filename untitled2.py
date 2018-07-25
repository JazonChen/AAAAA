# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:09:44 2018

@author: Administrator
"""
URL(unified统一 resourse资源 location位置)
练习8：保存淘宝数据（小组项目）
     1.每个组员爬取某个商品的100页数据  每个组员爬取的不同的城市，上海 北京 成都 郑州...
     2.保存淘宝商品信息（同练习6），并保存为csv格式
     3.每组组长合并各组员的数据 -后续班级合并数据
     
import urllib.request as r
import json
a=0
f1=open('南京.csv','w',encoding='gbk')

for i in range(0,100):
    try:
        a=i*44
        url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-global.a2227oh.d100&from=sea_1_searchbutton&catId=100&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&loc=%E5%8D%97%E4%BA%AC&s={}&ajax=true'.format(a)
        data=r.urlopen(url).read().decode('utf-8','ignore')
        f1.write(data+'\n')
        print('第'+str(i+1)+'页')
    except Exception as err:
        print('抓取失败')

f1.close()
 